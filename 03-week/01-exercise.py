# 1. Decipher Vigenere cipher when key is "DANGTIS"
# ŪUĖGK ŠKHNC RIŠFŽ PNŪTK CDUCG 
# ZVSLK ĘCNBC ŽDNČC ŠSŽNT RYEYB 
# AČGIL ČPĄVR MAĘLA BGNZS ŠOĖAD 
# RCSTŽ ĄKŪĮŽ PĮŲDŽ ĄDIKŠ FLDZI 
# KRKEY ZITUK FSŲBŽ ČKDCH KDKIŪ 
# LŪĮGR YIĮHI VZĖŠF ŽSŠĘD LVVID 
# CFMKŽ RKGGI GGIER ĮVSLK FZZHC 
# TCŽNŽ BTRAI ZJAŪN KČMKB HGĖGK 
# YDCŠT OĘTVS ŠDOĄT EĖĮLT RZAYL 
# STŽMŠ GZAKG GIGGA KRŽDH ŪLNRF 
# EODDŽ VTCCG VŽJŽČ CSTNŽ JAFHT 
# ŲTĮVS LKĮ   

import utils.global_vars as gv
import utils.vigenere_cipher as vc

gv.alphabet = "AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ"

key = "DANGTIS"
text = "ŪUĖGKŠKHNCRIŠFŽPNŪTKCDUCGZVSLKĘCNBCŽDNČCŠSŽNTRYEYBAČGILČPĄVRMAĘLABGNZSŠOĖADRCSTŽĄKŪĮŽPĮŲDŽĄDIKŠFLDZIKRKEYZITUKFSŲBŽČKDCHKDKIŪLŪĮGRYIĮHIVZĖŠFŽSŠĘDLVVIDCFMKŽRKGGIGGIERĮVSLKFZZHCTCŽNŽBTRAIZJAŪNKČMKBHGĖGKYDCŠTOĘTVSŠDOĄTEĖĮLTRZAYLSTŽMŠGZAKGGIGGAKRŽDHŪLNRFEODDŽVTCCGVŽJŽČCSTNŽJAFHTŲTĮVSLKĮ"

result = vc.decode_text(text, key)
print(result)