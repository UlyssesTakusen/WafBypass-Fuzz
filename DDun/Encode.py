# 另类字符集编码绕过_IBM037编码
import urllib
import sys

params = sys.argv[1]
charset= sys.argv[2]

def paramEncode(params="id=1", charset="IBM037", encodeEqualSign=False, encodeAmpersand=False, urldecodeInput=True, urlencodeOutput=True):
    result = ""
    equalSign = "="
    ampersand = "&"
    if encodeEqualSign:
       equalSign = equalSign.encode(charset)
    if encodeAmpersand:
       ampersand = ampersand.encode(charset)
    params_list = params.split("&")
    for param_pair in params_list:
       param, value = param_pair.split("=")
       if urldecodeInput:
          param = urllib.unquote(param).decode('utf8')
          value = urllib.unquote(value).decode('utf8')
       param = param.encode(charset)
       value = value.encode(charset)
       if urlencodeOutput:
          param = urllib.quote_plus(param)
          value = urllib.quote_plus(value)
       if result:
          result += ampersand
       result += param + equalSign + value
    return result

print(paramEncode(params,charset))
