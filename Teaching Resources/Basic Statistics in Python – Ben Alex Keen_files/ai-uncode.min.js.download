! function(e) {
	function i() {
		for (var e, i = 0, t = s.cookie.split(";"), a = /^\suncodeAI\.([^=]+)=(.*?)\s*$/, n = {}; i < t.length; ++i)(e = t[i].match(a)) && (n[e[1]] = e[2]);
		return n
	}

	function t(e) {
		e = Math.max(parseFloat(e || 1, 10), .01);
		var i = s.documentElement,
			t = function() {
				var e = s.createElement("div"),
					i = {
						width: "1px",
						height: "1px",
						display: "inline-block"
					};
				for (var t in i) e.style[t] = i[t];
				return e
			},
			a = s.createElement("div"),
			n = a.appendChild(t());
		a.appendChild(t()), i.appendChild(a);
		for (var r = a.clientHeight, o = Math.floor(c / r), l = o / 2, d = 0, h = [o]; d++ < 1e3 && (Math.abs(l) > e || a.clientHeight > r);) o += l, n.style.width = o + "em", l /= (a.clientHeight > r ? 1 : -1) * (l > 0 ? -2 : 2), h.push(o);
		return i.removeChild(a), o
	}

	function a(e) {
		for (var i, t = 0, a = (e || "").split(","), n = /(\d+(?:\.\d+)?)(px)?/i, r = []; t < a.length; ++t)(i = a[t].match(n)) && r.push(parseFloat(i[1], 10));
		return r.sort(function(e, i) {
			return e - i
		})
	}

	function n() {
		return "devicePixelRatio" in e ? e.devicePixelRatio : "deviceXDPI" in e && "logicalXDPI" in e ? e.deviceXDPI / e.logicalXDPI : 1
	}
	if (navigator.cookieEnabled) {
		var r = "uncodeAI",
			o = ";path=/",
			s = document,
			c = e.innerWidth,
			l = screen.width,
			d = screen.height,
			h = {},
			p = !0;
		h = i(), void 0 !== h.images && (p = !1);
		for (var u = 0, g = s.getElementsByTagName("script"); u < g.length; ++u)
			if (g[u].id == r) {
				var v = n(),
					m = "2880",
					f = "2880";
				if (s.cookie = r + ".screen=" + l + o, !g[u].getAttribute("data-disable-images")) {
					var b = a(g[u].getAttribute("data-breakpoints-images")),
						k = Math.max(l, d),
						x = null;
					do {
						if (k > (x = b.pop())) break;
						m = x, v > 1 && (f = x * v)
					} while (b.length)
				}
				if (f > 2880 && (f = 2880), s.cookie = v > 1 ? r + ".images=" + f + o : r + ".images=" + m + o, h = i(), cssBreakpoint = h.css || "-", !("css" in h && h.css && "-" != h.css || g[u].getAttribute("data-disable-css"))) {
					var w = c / t(parseFloat(g[u].getAttribute("data-em-precision") || .5, 10) / 100);
					cssBreakpoint = l + "x" + d + "@" + Math.round(10 * w) / 10
				}
				s.cookie = r + ".css=" + cssBreakpoint + o;
				break
			}
		p && void 0 !== h.images && window.location.reload()
	}
}(this);