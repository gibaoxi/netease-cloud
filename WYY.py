﻿import requests#10-9


url1="https://music.163.com/weapi/user/level?csrf_token=a4dbd8dedde42e9cea293434b3544369";

data1='params=QRUrzYLu3bjp%2FVbGVikd3LhS%2FmUJ2Zxnkv8eNp7kw2qENYW3E8dURviEcynl9l7UMV2yDfrPFPduV0YaUuH6HyGC9H72g75xjEdvSxhnfp7vRyPHtwJR0aBEIrAfS8mW&encSecKey=2f92afcca5689bfe9dfa38922bb7154768bfc1dded83b88b6d4bc8645f81835b491553be6db2e3c25bdc4fe510e9ce63853dd57459bc056aa8129091fe2727371729ab208e1f197907e3f1b403d6585d9eb760a84836b5de49347dd9f305bc2be5519acf713917f948f6e12e3e4acfc5497c5b936827237b673b4ca75800129a'


headers1={
    "host":"music.163.com", 
"Content-Type": "application/x-www-form-urlencoded",
"content-length": "418",
"accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36",

"accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",

    "Sec-Fetch-Mode": "cors",

"Sec-Fetch-Site": "same-origin",

"Sec-Fetch-Dest": "empty",



     "origin": "https://music.163.com",    

"referer": "https://music.163.com/user/level", 

            "Accept-Encoding": "gzip,deflate",
    "cookie":"NMTID=00OZce1YxsPx1fLzE50iTgvYspG8G4AAAGLb7PVfA;JSESSIONID-WYYY=DiVGuySEkE2x804%2B67zya%2B9WCNt2n8NzNvJX5KRTM1%2BilBY%2BKyO4qtyn0Knvf3%2B%5C2aGk5Y%2BEld%2Fy%2B%5CF1l9t9ls2425WE%2FTol1bH53FT5%2BHghuccv5hC7vwHA4QPImhybz%5CuHaIHFJVF1AOxsSia8aUhpgvY9vXympoviP8EC7dJaDHjB%3A1698387941342;_iuqxldmzr_=32;_ntes_nnid=d7e22e13c884a41019a9ce7367da4047,1698386141426;_ntes_nuid=d7e22e13c884a41019a9ce7367da4047;WEVNSM=1.0.0;WNMCID=vgfjnk.1698386147578.01.0;ntes_utid=tid._.QXwt4FHtwHlAQwEQFELVnziq3mAVwGCH._.0;sDeviceId=YD-Rt5Xy5aUSXlBEgREQVfUjzyujmBEhHDT;__snaker__id=2AEWpbcaPFDGkg3j;WM_NI=UaD%2FSUemjFmn7Q8opCsqHfzPRIsZAHydxX6rjwF6EIs%2BgvQ0phIc1az1jmzwmJx51TYrKz6BhR23EJnYPvrB2692CYqRwlp9pZSyw89epdR5hyL3aTIQklJl7l8vQfkRNmw%3D;WM_NIKE=9ca17ae2e6ffcda170e2e6eed8d76193eea4d3d34a83b48ea2d85f839a8fb0c873aeb3e19bf05a91bb88afb22af0fea7c3b92a97bf8cd0d25fa7b3a6a7f066f58ff890f349b1af8887f95c9297bdbbc444bbbcb8b9b57aaaa98ad7c843b1f5a997d43cb4b88784b46bbaefa68ef97daf96b8d6b4609bae859bb54aac8efed4c842ae87a097f14af2eaf7d3c253b38eb98df333b4869d9af634fbbbc085d13faca784d4e4608b8fa58dc968f5b4f897d46ea98e828ef637e2a3;WM_TID=%2FaAZovSTwuxERVVERUPVz2m%2F2iRTODJy;gdxidpyhxdE=PJY5xJLBvRYay0ZRhn3%2F3cqu4lE5N1%2BZuCitMv9z2SD5XIydhiTktJGq1ZeYPGtTeSEQ6%5CXwiJhY%2FDGXmBGV%2FSqGL7VXMHiYH8GKLtkjfDhzNc8o5Aud8iqN3TM3pN1UKVD0T0Vsk%2B4gB4zf%5CXSt87uVwqt8lzBw2HnhtDkX4OVl%2FSTJ%3A1698387058096;YD00000558929251%3AWM_NI=El3kc0KUiN1JeOxTvplB5G%2BsgIAdUI4ZCzPiJ5rhJVJwHhEpzOYdDNVasKXITJn7ym9dshRG%2B982FXN5NDebOh40Hma1ORs%2F1aIziHesZBM2zBTvbKI9c1WjLrvVCORnMzY%3D;YD00000558929251%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eeacb85086ab9bd9b16ab2e78eb3d14e939a8a86c562bbedbf8be94e91eff984c82af0fea7c3b92a87b4fd8ce23c898ba7afb442a791b8b5f57cb09efba8aa79a5978f85d843f8868d9bd3638aebbe89c95e8aa98889c87cba919785c74696bfbdacdb439896a2d8fc67fbbcbd89d14de9e7f8d3c5548eeb82a5e86a8db8fcd1cb67a3ef81b3f225f3bf879bec44a7ad96a3d03aba9e9c97e1418be7add2d66290aebab7c24592b2839bdc37e2a3;YD00000558929251%3AWM_TID=U82CjE5sHHlBFAQQUAKUmiiuiiBDkuMF;__csrf=148b728dff3e8e4634618ba579cd3545;MUSIC_U=003F933E7B0C56637E2077DE13D1B3E1ACF85D22D18312D0D7FB13191F4FE755F3797D941C1F8C74A95C7634EE825BCA73736D8542655D4409619192B150DF5D1E839F64F0CB5C764EE7ABE2B61EC9890A33E7B12C6DCB5539153C8327A194C2D170BEB7F05DABAE1B7739849151FD030114ED36D4D896367B44727B7EBFA5908217C9B5EF22128183500685D310602F9B6DBEF8BFA85257B4D5E7537F2466CDF5598A30A5AC59EC12307FBF23E0536B33A627FC65A48D4C6CD27755D16C93500E855BA3E09F95277C0684B6948F2953953303C2862DD45FDACAC02683DB3AEC5F16C4C9C3171AC96658D6B444BEB3CE74967D37F72A49206663351A323CB2853C3E9A15A02BEE4475B858AEB938B813774CAF2877A5507C96694638EFC6550BBFB59E3A8A726B868B2665610BAE7057F2683289E0559C5E24A1D2F7846B8DD9147107DD1A8BA242A14B66D15EC0BBD930E6B3D3E33AB045ECEA989BE625300FC9;__remember_me=true;ntes_kaola_ad=1"}



headers3={
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "Cache-Control": 'no-cache',
"User-Agent": "Mozilla/5.0 (Linux; Android 7.0; SLA-AL00 Build/HUAWEISLA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2898 MMWEBSDK/191102 Mobile Safari/537.36 MMWEBID/4984 MicroMessenger/7.0.9.1560(0x27000933) Process/tools NetType/WIFI Language/zh_CN ABI/arm32",
            "accept": "*/*",
            "connection": "Keep-Alive",
            "Accept-Encoding": "gzip,deflate",
"origin": "https://prodev.m.jd.com",
"cookie":"__jdc=123;mba_muid=16656250288711537561796;shshshfpb=jZWYM7fsK_oOaAVpf1hAFMQ;shshshfpa=f7dfe904-13eb-dadf-d735-e9b395f54063-1665625038;visitkey=39109935208295376;retina=1;webp=1;sc_width=360;fingerprint=198f6505b26e47babc312c32a237527c;deviceVersion=7.0.20.1781%280x27001438%29;deviceOS=android;deviceOSVersion=7.0;deviceName=WeiXin;appCode=msd95910c4;share_cpin=;share_open_id=;share_gpin=;shareChannel=;source_module=;erp=;rurl=https%3A%2F%2Fwqsh.jd.com%2Ffsqd_02%2Findex%2Findex.html%3Fptag%3D17005.2.140;TrackID=208ZkhONJuT_b_2gp3GAJ0ACJFH3EUiFCqROCxO5ap9eUraHR2hUD-EomrglwHW_zXfu5MQ7iTV9AMKFKC6MUTdkv4fUYIjTmJ93b3sr6FfIlDg-78Im0TmgZujES598gfe7nGftm2sSp0Z1IV_IvtmmwFaI3UWXorwgSdZ8_VQ;buy_uin=6243189844;jdpin=jd_MQpaTEVYUTcD;mcossmd=c5e7245eefdd843918c65946369a6f23;nickname_base64=;open_id=oTGnpnJNnYfeM8QCeYdyGIg5iACw;picture_url=;pin=jd_MQpaTEVYUTcD;pinId=XGISOrPMzFweTFlcwCs_4Q;pinsign=22ed8529b51ded49733c0b2c89cf4048;sex=0;wq_skey=za2B103486161F0F5D80F66755827E23B8500810176E2BD00C9709DF22C82C809A5D945208D283E3CCAED86C56ADA51791989C478BA9B85E6F28AB3BC9B064962FB36528AC6EF4410F5D0F59C72E2532AF;wq_uin=6243189844;wq_unionid=oCwKwuCXZzs9KeB2CucYG0rwWJUY;wx_nickname=jd_user;unpl=JF8EAKdnNSttCBwDUE9WHRcUSV9UW1QOSx4BPDAHBA4LTFRXHwZJGhB7XlVdXhRLFh9vYBRUW1NKVA4fAysSE3tdVV9cAUMSAGphNWRaWEIZRElPKxEQe11Vbl0PTBMEbGMEV1RRTVQFHwAdFhdLW1xZbThMFwpfVzVWX19IUjUaMhsXGEhaUl9eC0InSAFmSFRaX09TBh8DGBsZTV1UWl8OTxADaW8CZFxoSA;openid2=2A1456B73D51B6193A311180F8D93327B2AD08EB51F7D9FE1C8EC284C837B2BBD71EE8A7E6DE4464D3D5611236935A1E;wxa_level=1;jxsid=16663133734199468141;__jdv=68990090%7Cweixin%7Ct_1000072662_17005_001%7Cweixin%7C-%7C1666313374925;PPRD_P=LOGID.1666312882491.1890971811-UUID.16663127024471338252831-EA.17005.2.140;shshshfp=1c8544c05a7110052711f4e25c5799b0;__jda=123.16656250288711537561796.1665625028.1666313374.1666316751.11;cid=9;__jxjda=68990090.1665910894731561532902.1665910894.1666312709.1666316769.3;jxsid_s_u=https%3A//home.m.jd.com/myJd/newhome.action;network=wifi;equipmentId=CRE356AGHD3SDWHLBTVYDODZAV2A4ZWDWFEQ73KIVBDSSRMEJATNUEWFZ2FKWYZP77RLAZDODJSF7P6ODAOJDZGVQM;TrackerID=QawgMVGLmIxQIl1ssPaTaIFecBDQnEz6Rlc9WiHCOUiqqYW8nNCY4dCHxa2CHED1Nwf9G2PtuM8g2PSUj97OVTbQg2dG5-pImLSVuFcKX5ycn--WrUCipmckBmkgg9diaQefn0Me9WKbTVCQXJwukg;pt_key=AAJjUfnsADACMEAT8uZwhwXrblFCph_QDPBfmo8Oxn6skQxYefUoMoNM9oPI9e7vyrwyBVn9jjg;pt_pin=jd_MQpaTEVYUTcD;pt_token=6412otds;pwdt_id=jd_MQpaTEVYUTcD;sfstoken=tk01m76361b17a8sMXgzeDJ5ajJ3A481CET+/3I2Oag2ozbDuWyfhU0jmOF4jxv+Io4o3ZsTcT5N0y+JllQWJCRi+Rcc;__wga=1666316784968.1666316769685.1666312886862.1665625050126.2.6;jxsid_s_t=1666316785423;shshshsID=550c09516d8737a620f326a76be7f29f_2_1666316786210;wqmnx1=MDEyNjM3MnQuL3Z4NjM4OTI3bCggZFMwL1MwQWI3SGlrczBlMyA4RTBvYTNNOGNlLjc3KXNzaDN5SWFDYTRZZi00WUQjKEg%3D;__jdb=123.6.16656250288711537561796|11.1666316751;mba_sid=16663167511236267735635829486.4;__jd_ref_cls=MCommonBottom_My;"

      
            }


headers4={
         "host":"music.163.com",

            "upgrade-insecure-requests":"1 ",

            "User-Agent": "Mozilla/5.0 (Linux; Android 9; JKM-AL00 Build/HUAWEIJKM-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3262 MMWEBSDK/201201 Mobile Safari/537.36 MMWEBID/3993 MicroMessenger/8.0.1840(0x28000036) Process/toolsmp WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm64",


            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            
            "Accept-Encoding": "gzip,deflate",

"Sec-Fetch-Mode": "navigate",

"Sec-Fetch-Site": "same-origin",

"Sec-Fetch-Dest": "iframe",


"sec-fetch-user": "?1",


"accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
"cookie":"WEVNSM=1.0.0;WNMCID=lqbped.1681524657589.01.0;NMTID=00ONfgdaXT8mIs9akzjp886pdXtcekAAAGHgq4BRw;JSESSIONID-WYYY=2AZ0AhFUKIB45zZMHu6diDBHJEjDsu%2Bowuv73cGxJ%2BiwIXXNAd%2B%5C8x%2BHpYQc42%2Fwi0Z%5CM%2BFUgtm%2B%2FRPKiwuKZu3k%5C9%2Bv5kh4ldIw9TjdzPvYoQ%2BJM8AhYMjtWkna%5Cvb2N%2BqPvA4kXj%2FnKUdR90PRgvr8WjDfcyABkwAJ8bUPMVQxdqkZ%3A1681526457663;_iuqxldmzr_=33;_ntes_nnid=c39b4fac45b11677590726cf23095a60,1681524657808;_ntes_nuid=c39b4fac45b11677590726cf23095a60;WM_NI=TL6j%2BIO8k2GDDpdBxPN1AzKEQBfZyDDLZuqA%2FaKuG4AkItOaQVyiXgK9OZmSG55PWD4Xd%2BsgWFERKW1HPo5qeKdy7fLxWTdTXkZ%2BQ3HABWBJD6PV9E85rb2AkU5MzFUVaDU%3D;WM_NIKE=9ca17ae2e6ffcda170e2e6eeafbc3a95b0fc83db64989a8ba2d55f929f9e86c16af89a86d3e56495ae88a2cb2af0fea7c3b92a9894fa8baa438de8a5d3c65088b0aca3fb5c8eef8f9bca4f939eaabbfc5088949696f44bedbf8596c64083b58795ce6b938ab78adb6d89e781bbf05985ebfbb1d650f888acccf26d959a8bb3ca5df398a090b87ba795ac9ab66e90a899b5e7609cb596ccd4398c9f8eb8c14288eaa0b7bc4ffcebbe83b14ba98bfbaef94e978aafa5d837e2a3;WM_TID=D7ujTHoVYGREARFRBAbQLpEdza1X8W3N;__snaker__id=C68oHEdkuzgHFQBW;gdxidpyhxdE=58kPdPuJakXSyn%5CentsHm7gn1vV%2Bd%5C7ejelWWES6SxHYq%5CE4plyX53aZJnzqkr3vh95N2T6Dev06ZtDlHm91p%2FWBlH2hJKGyeo9Xq5tKm8pqDI1i97IIPAHRaGZmaXX1wLkuyE7KY7ug3sh7U%2FK%2BvLz%5C7Sge%5Cj%2BTYWkdlOe2hqyjOE8A%3A1681525573124;YD00000558929251%3AWM_NI=H%2B1kRgOQ5f77Onah9N4gofqFed0jHu8KO8%2Ffj94tB%2F8fjsyLhvMgCfOqt2mobz4vyw1mn7PBxTqQQMZyG07F3kHIBNyo1OQfRtN0sOvbAE99wU5Xi%2B%2B5%2FpJhLktpyhGbYW8%3D;YD00000558929251%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eeb0d83991f198d2c46ea1b08ea6c54e878a9b87c86bfb9fac8bca7d89f5bc8fed2af0fea7c3b92a8cf5ff8cd16d8d8ffb87b63d8db2af89bc46f8b9a187f44ea7bc008bcb7ffc9581d9ae6eaae7fc95c125fcbaa694fc48acaa8388c26e8dafbcd3f065a2a6fc97fc7df3b3a2d8d34abc8cbfb2d4479aa789d1b64ef1b588aac146bbb1ffb0d46e92ac82d1f245b6be8fa6bc33b58bfbb9ec21e9ebe191c96490b5bc91fc6485be97b8bb37e2a3;YD00000558929251%3AWM_TID=Bg98ZYGkUARBUEFBFULAPpVdyawP%2Bpzz;__csrf=e3b1a58b730053cc27bb895fabc9fe0c;__remember_me=true;MUSIC_U=207cefb9caf33ecb3f3df5092aca25cdeda48ce278e2b50a23753e8d32df73f1993166e004087dd3bc4b00e1707690e2edc0b299125e70cd989b2eba55c756ffb44b8fb6d645dcdfd4dbf082a8813684;ntes_kaola_ad=1;"

}

            
response1= requests.post(url=url1,data=data1,headers=headers1)
print(response1.text)




def notice(content):
    token ="c204e4622c9f4e3e8bf06591c7f6e89d"
    title = "网易云cs"
    url = f"http://www.pushplus.plus/send?token={token}&title={title}&content={content}&template=html"
    response9=requests.request("GET", url)
    print(response9.text)
notice(response1.text)

