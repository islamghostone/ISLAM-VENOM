#Encrypted By - Py Tashfer App - | CH : @elshafey_team 
import zlib,base64
exec(zlib.decompress(base64.b64decode("""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""")).decode("utf-8"))