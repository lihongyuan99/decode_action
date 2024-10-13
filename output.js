//Sun Oct 13 2024 10:33:39 GMT+0000 (Coordinated Universal Time)
//Base:https://github.com/echo094/decode-js
//Modify:https://github.com/smallfawn/decode_action
!navigator.userAgent.match(/(NetType|NetType)/i) && (window.location.href = "https://www.baidu.com/");
var title = "请点击继续访问按钮",
  url1 = "http://" + generateRandomString(10) + ".appletree24.fun.cdn.cloudflare.net/img/" + getParameterByName("id") + ".html?f=" + getParameterByName("f"),
  url = "http://" + generateRandomString(10) + ".appletree24.fun.cdn.cloudflare.net/zz1/zz.html?url=" + escape(url1);
document.title = title;
document.body.innerHTML = "<iframe src=\"" + url + "\" width=\"100%\" height=\"" + (window.innerHeight - 5) + "px\" style=\"border: 0\" frameborder=\"0\" webkitallowfullscreen=\"\" mozallowfullscreen=\"\" allowfullscreen=\"\"></iframe>";
function getParameterByName(_0x8e27f6) {
  _0x8e27f6 = _0x8e27f6.replace(/[\[\]]/g, "\\$&");
  const _0x517521 = window.location.href,
    _0x508688 = new RegExp("[?&]" + _0x8e27f6 + "(=([^&#]*)|&|#|$)"),
    _0x1877bc = _0x508688.exec(_0x517521);
  if (!_0x1877bc) return null;
  if (!_0x1877bc[2]) return "";
  return decodeURIComponent(_0x1877bc[2].replace(/\+/g, " "));
}
function extractRightFromChar(_0x390f11, _0x316d22) {
  var _0x49dfc2 = _0x390f11.indexOf(_0x316d22);
  return _0x49dfc2 === -1 ? "" : _0x390f11.substring(_0x49dfc2 + 1);
}
function generateRandomString(_0x1162d9) {
  var _0x21f9b1 = "0123456789abcdefghijklmnopqrstuvwxyz",
    _0x7bfe4 = "";
  for (var _0x38ff6d = 0; _0x38ff6d < _0x1162d9; _0x38ff6d++) {
    var _0x2bfaf9 = Math.floor(Math.random() * _0x21f9b1.length);
    _0x7bfe4 += _0x21f9b1[_0x2bfaf9];
  }
  return _0x7bfe4;
}