// Motor mínimo para ver las pantallas del lienzo de diseño en cualquier navegador.
// Entiende lo que usan los archivos .dc.html: {{huecos}}, <sc-if>, <sc-for>,
// eventos onClick y setState. Sin dependencias.
(function () {
  var HOLE = /\{\{([^}]+)\}\}/g;
  var WHOLE = /^\s*\{\{([^}]+)\}\}\s*$/;

  function lookup(scope, expr) {
    expr = expr.trim();
    if (expr === 'true') return true;
    if (expr === 'false') return false;
    if (expr === 'null') return null;
    if (/^-?\d+(\.\d+)?$/.test(expr)) return Number(expr);
    var parts = expr.split('.');
    var v = scope[parts[0]];
    for (var i = 1; i < parts.length && v != null; i++) v = v[parts[i]];
    return v;
  }

  function interp(str, scope) {
    return str.replace(HOLE, function (_, e) {
      var v = lookup(scope, e);
      return v == null ? '' : String(v);
    });
  }

  function renderChildren(parent, scope, out) {
    for (var c = parent.firstChild; c; c = c.nextSibling) renderNode(c, scope, out);
  }

  function renderNode(node, scope, out) {
    if (node.nodeType === 3) {
      out.push(document.createTextNode(node.data.indexOf('{{') >= 0 ? interp(node.data, scope) : node.data));
      return;
    }
    if (node.nodeType !== 1) return;
    var tag = node.localName;
    if (tag === 'sc-if') {
      var m = WHOLE.exec(node.getAttribute('value') || '');
      if (m && lookup(scope, m[1])) renderChildren(node, scope, out);
      return;
    }
    if (tag === 'sc-for') {
      var ml = WHOLE.exec(node.getAttribute('list') || '');
      var list = (ml && lookup(scope, ml[1])) || [];
      var as = node.getAttribute('as') || 'item';
      for (var k = 0; k < list.length; k++) {
        var s = Object.create(scope);
        s[as] = list[k];
        s.$index = k;
        renderChildren(node, s, out);
      }
      return;
    }
    var el = document.createElementNS(node.namespaceURI, tag);
    for (var i = 0; i < node.attributes.length; i++) {
      var a = node.attributes[i];
      var name = a.name;
      var val = a.value;
      if (name.indexOf('hint-') === 0) continue;
      var whole = WHOLE.exec(val);
      if (name.slice(0, 2) === 'on') {
        var fn = whole ? lookup(scope, whole[1]) : null;
        if (typeof fn === 'function') el.addEventListener(name.slice(2), fn);
        continue;
      }
      var v = whole ? lookup(scope, whole[1]) : (val.indexOf('{{') >= 0 ? interp(val, scope) : val);
      if (name === 'defaultvalue') name = 'value';
      if (name === 'defaultchecked') name = 'checked';
      if (v === false || v == null) continue;
      if (v === true) v = '';
      v = String(v);
      if (name === 'href') v = v.replace(/\.dc\.html/g, '.html');
      el.setAttribute(name, v);
    }
    var kids = [];
    renderChildren(node, scope, kids);
    for (var j = 0; j < kids.length; j++) el.appendChild(kids[j]);
    out.push(el);
  }

  window.DCLogic = function (props) {
    this.props = props || {};
    this.state = null;
  };
  window.DCLogic.prototype.setState = function (patch) {
    this.state = Object.assign({}, this.state || {}, patch);
    if (window.DC._render) window.DC._render();
  };

  window.DC = {
    mount: function (Comp) {
      var tpl = document.getElementById('tpl').content;
      var app = document.getElementById('app');
      var comp = new Comp({});
      window.DC._render = function () {
        var vals = comp.renderVals() || {};
        var out = [];
        renderChildren(tpl, vals, out);
        while (app.firstChild) app.removeChild(app.firstChild);
        for (var i = 0; i < out.length; i++) app.appendChild(out[i]);
      };
      window.DC._render();
    }
  };
})();
