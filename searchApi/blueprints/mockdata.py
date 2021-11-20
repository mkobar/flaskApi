# flake8: noqa: E501
verbose = 9  # all the debug prints

# use SerpAPI format for easy digest
data = {
    "search_metadata": {},
    "search_parameters": {},
    "search_information": {},
    "ads": [],
    "local_map": {},
    "local_results": [],
    "related_questions": [],
    "answer_box": {},
    "organic_results": [],
    "related_searches": [],
    "pagination": {},
}

# mockdata[] = {}

mockDataHtml = b"<html><head><title>Mocked</title></head><body><h1>Search Results: Mocked</h1></body></html>"

mockDataKittensHtml = b"<html><head><title>Kittens</title></head><body><h1>Search Results: Kittens</h1></body></html>"

mockDataCatsHtml = b"<html><head><title>Cats</title></head><body><h1>Search Results: Cats</h1></body></html>"

mockDataCatsHtml2 = b"""
<!DOCTYPE doctype html><head></head><body>
<p>About 5,430,000,000 results<br>
<h2>Related Searches</h2>
<a href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=cats+musical&amp;sa=X&amp;ved=0ahUKEwio09aww5HgAhXGJt8KHedtApgQ1QIIYCgA">cats <b>musical</b></a><br><br>
<a href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=cats+the+musical+tour+2018&amp;sa=X&amp;ved=0ahUKEwio09aww5HgAhXGJt8KHedtApgQ1QIIYSgB">cats <b>the musical tour 2018</b></a><br><br>
<a href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=cats+breeds&amp;sa=X&amp;ved=0ahUKEwio09aww5HgAhXGJt8KHedtApgQ1QIIYigC">cats <b>breeds</b></a><br><br>
<a href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=cats+musical+characters&amp;sa=X&amp;ved=0ahUKEwio09aww5HgAhXGJt8KHedtApgQ1QIIYygD">cats <b>musical characters</b></a><br><br>
<a href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=cats+broadway&amp;sa=X&amp;ved=0ahUKEwio09aww5HgAhXGJt8KHedtApgQ1QIIZCgE">cats <b>broadway</b></a><br><br>
<a href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=cats+the+musical+cast&amp;sa=X&amp;ved=0ahUKEwio09aww5HgAhXGJt8KHedtApgQ1QIIZSgF">cats <b>the musical cast</b></a><br><br>
<a href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=cats+movie&amp;sa=X&amp;ved=0ahUKEwio09aww5HgAhXGJt8KHedtApgQ1QIIZigG">cats <b>movie</b></a><br><br>
<a href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=cats+musical+london&amp;sa=X&amp;ved=0ahUKEwio09aww5HgAhXGJt8KHedtApgQ1QIIZygH">cats <b>musical london</b></a><br><br>
<h2>Related Questions</h2><h2>Organic Results</h2>
<a href="/url?q=https://www.catsthemusical.com/&amp;sa=U&amp;ved=0ahUKEwio09aww5HgAhXGJt8KHedtApgQFggUMAA&amp;usg=AOvVaw0fN9vOOrvsJyJ68E-LStF6">
<b>Cats</b> the Musical - Official Website &amp; Tickets</a><br>
<span class="st">The official home of Andrew Lloyd Webber's world-famous, family-favourite <br/>
musical <b>CATS</b> - Tickets from $20 &amp; NO booking fee!</span><br><br>
<a href="/url?q=https://en.wikipedia.org/wiki/Cats_(musical)&amp;sa=U&amp;ved=0ahUKEwio09aww5HgAhXGJt8KHedtApgQFggeMAE&amp;usg=AOvVaw3YY0yVIcC9HpUHezxpk2mG"><b>Cats</b> (musical) - Wikipedia</a><br>
<span class="st"><b>Cats</b> is a sung-through musical composed by Andrew Lloyd Webber, based on <br/>
Old Possum's Book of Practical <b>Cats</b> by T. S. Eliot. The musical tells the story of a<br/>
 ...</span><br><br><a href="/search?q=cats&amp;hl=en&amp;gl=us&amp;ie=UTF-8&amp;prmd=ivnsb&amp;source=univ&amp;tbm=nws&amp;tbo=u&amp;sa=X&amp;ved=0ahUKEwio09aww5HgAhXGJt8KHedtApgQqAIIKQ">
News for <b>cats</b></a><br>
 <span class="st">Taylor Swift gave fans an update from the set of the "<b>Cats</b>" movie on Monday. In a <br/>
pair of selfies posted on her Instagram, the pop superstar ...</span><br><br>
<a href="/url?q=http://www.vetstreet.com/cats/&amp;sa=U&amp;ved=0ahUKEwio09aww5HgAhXGJt8KHedtApgQFggyMAU&amp;usg=AOvVaw0_tmV-Th-35Lg81tIpjzso"
>Complete Guide to Caring for <b>Cats</b> | <b>Cat</b> Breed Information, <b>Cat</b> ...</a><br>
<span class="st">Your <b>cat's</b> online owners manual, featuring articles about breed information, <b>cat</b> <br/>
selection, training, grooming and care for <b>cats</b> and kittens.</span><br><br>
<a href="/url?q=https://www.purina.com/cats/cat-breeds&amp;sa=U&amp;ved=0ahUKEwio09aww5HgAhXGJt8KHedtApgQFgg4MAY&amp;usg=AOvVaw0zVTeOx_FeB_r7bFXDmBic"><b>Cat</b> Breed Collection | Purina</a><br>
<span class="st">Trying to decide what type of <b>cat</b> is right for you and your family? Browse through <br/>
our list of popular <b>cat</b> breeds, and find the best breed for your lifestyle.</span><br><br>
<a href="/url?q=http://www.animalplanet.com/pets/cats/&amp;sa=U&amp;ved=0ahUKEwio09aww5HgAhXGJt8KHedtApgQFgg-MAc&amp;usg=AOvVaw3fRt0DAEQluZSOanBbaX9C"><b>Cats</b> | Animal Planet</a><br>
<span class="st">Explore our guide to <b>cats</b>, kittens and their habitats. Learn about over a hundred <br/>
different <b>cat</b> breeds and how to deal with troubled <b>cats</b>.</span><br><br>
<a href="/search?ie=UTF-8&amp;q=cats&amp;tbm=isch&amp;source=univ&amp;gl=us&amp;hl=en&amp;sa=X&amp;ved=0ahUKEwio09aww5HgAhXGJt8KHedtApgQsAQIRA">Images for <b>cats</b></a><br>
<span class="st">WebMD veterinary experts provide comprehensive information about <b>cat</b> health <br/>
care, offer nutrition and feeding tips, and help you identify illnesses in <b>cats</b>.</span><br><br>
<a href="/url?q=https://www.webmd.com/pets/cats/default.htm&amp;sa=U&amp;ved=0ahUKEwio09aww5HgAhXGJt8KHedtApgQFghQMA0&amp;usg=AOvVaw39TVq-F9zC_JIr8qnoPAtq"
<b>Cat</b> Health Center | <b>Cat</b> Care and Information from WebMD</a><br>
<span class="st">Everything you need to know about how to adopt a <b>cat</b>, bringing your new <b>cat</b> <br/>
home, <b>cat</b> health and care and more!</span><br><br>
<a href="/url?q=https://www.petfinder.com/cats/&amp;sa=U&amp;ved=0ahUKEwio09aww5HgAhXGJt8KHedtApgQFghVMA4&amp;usg=AOvVaw3zeuNo8WnICBwLNA_AsodM">
<b>Cats</b>: Adoption, Bringing A <b>Cat</b> Home and Care - Petfinder</a><br>
<span class="st"><span class="f">
<span class="nobr">Dec 24, 2016</span> - <span class="nobr">10 min</span> - <span class="nobr">Uploaded by Tiger Productions</span></span><br/>
<b>Cats</b> are simply the funniest and most hilarious pets, they make us laugh all the  time! Just look <b>...</b></span><br><br>
<a href="/url?q=https://www.youtube.com/watch%3Fv%3D5dsGWM5XGdg&amp;sa=U&amp;ved=0ahUKEwio09aww5HgAhXGJt8KHedtApgQtwIIXDAP&amp;usg=AOvVaw2pJRsHdsgg3_comjo5pEOw">
<b>Cats</b> are so funny you will die laughing - Funny <b>cat</b> compilation ...</a><br>
</body></html>"""

mockDataCarsHtml = b"""
<!doctype html>
<html itemscope="" itemtype="http://schema.org/SearchResultsPage" lang="en">
<head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type">
<meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image">
<noscript><meta content="0;url=/search?q=cars&amp;hl=en&amp;gl=us&amp;ie=UTF-8&amp;gbv=1&amp;sei=16NHXKPaGOKU0gKPk6KACw" http-equiv="refresh">
<style>table,div,span,p{display:none}</style>
<div style="display:block">Please click <a href="/search?q=cars&amp;hl=en&amp;gl=us&amp;ie=UTF-8&amp;gbv=1&amp;sei=16NHXKPaGOKU0gKPk6KACw">
here</a> if you are not redirected within a few seconds.</div></noscript>
<title>cars - Google Search</title>
<style>#gbar,#guser{font-size:13px;padding-top:1px !important;
}#gbar{height:22px}#guser{padding-bottom:7px !important;text-align:right}.gbh,.gbd{border-top:1px solid #c9d7f1;font-size:1px
}.gbh{height:0;position:absolute;top:24px;width:100%}@media all{.gb1{height:22px;
margin-right:.5em;vertical-align:top}#gbar{float:left}}a.gb1,a.gb4{text-decoration:underline !important}a.gb1,a.gb4{color:#00c !important
}.gbi .gb4{color:#dd8e27 !important}.gbf .gb4{color:#900 !important}
</style><style>.star{float:left;margin-top:1px;overflow:hidden}.ybhkme{font-size:11px}.j{width:34em}body,td,div,a{
font-family:arial,sans-serif;tap-highlight-color:rgba(255,255,255,0)}body{margin:0}a img{border:0}#gbar{float:left;
height:22px;padding-left:2px;font-size:13px}.gsfi,.gsfs{font-size:17px}.w,.q:active,.q:visited,.tbotu{color:#11c}a.gl{
text-decoration:none}#foot{padding:0 8px}#foot a{white-space:nowrap}h3{font-size:16px;font-weight:normal;margin:0;
padding:0}#res h3{display:inline}.hd{height:1px;position:absolute;top:-1000em}.g,body,html,table,.std{font-size:13px}.
g{margin-bottom:23px;margin-top:0;zoom:1}ol li,ul li{list-style:none}h1,ol,ul,li{margin:0;padding:0}.e{margin:
2px 0 0.75em}#leftnav a{text-decoration:none}#leftnav h2{color:#767676;font-weight:normal;margin:0}#nav{
border-collapse:collapse;margin-top:17px;text-align:left}#nav td{text-align:center}.nobr{white-space:nowrap}.ts{
border-collapse:collapse}.s br{display:none}.csb{display:block;height:40px}.images_table td{line-height:17px;
padding-bottom:16px}.images_table img{border:1px solid #ccc;padding:1px}#tbd,#abd{display:block;min-height:1px}#abd{
padding-top:3px}#tbd li{display:inline}.TIrJXe,.UU5df{margin-bottom:8px}#tbd .tbt li{display:block;font-size:13px;
line-height:1.2;padding-bottom:3px;padding-left:8px;text-indent:-8px}.tbos,.b{font-weight:bold}em{font-weight:bold;
font-style:normal}.mime{color:#1a0dab;font-weight:bold;font-size:x-small}.soc a{text-decoration:none}.soc{color:#808080
}.ul7Gbc{color:#e7711b}#Db7kif{border:1px solid #e0e0e0;margin-left:-8px;margin-right:-8px;padding:15px 20px 5px}.mrH1y
{font-size:32px}.PZ6wOb{color:#777;font-size:16px;margin-top:5px}.gwrItc{color:#777;font-size:14px;margin-top:5px}
.SVob4e{border:1px solid #e0e0e0;padding-left:20px}.mYu5Hb{border:1px solid #e0e0e0;padding:5px 20px}#vob{border:
1px solid #e0e0e0;padding:15px 15px}#ZjIC2e{font-size:22px;line-height:22px;padding-bottom:5px}#vob_st{line-height:1.24
}.DfLGHd{border-width:1px;border-style:solid;border-color:#eee;background-color:#fff;position:relative;margin-bottom:
26px}.uRIxYb,.NjTIc,.PftIHd,.DXoZmb{font-family:Arial;font-weight:lighter}.uRIxYb{margin-bottom:5px}.uRIxYb{font-size:
xx-large}.NjTIc{font-size:medium}.PftIHd{font-size:large}.DXoZmb{font-size:small}.DfLGHd{margin-left:-8px;margin-right:-15px;
padding:20px 20px 24px}.ernfsc{border-spacing:0px 2px}.D3VFNd{max-width:380px;text-overflow:ellipsis;
white-space:nowrap;overflow:hidden;padding-left:0px}.c1Ujmc{padding-left:15px;white-space:nowrap;color:#666}.EjZtie{padding-left:0px
}.SFt5jb{color:#212121}.Pt7r9e{color:#878787}.bkcGhd{color:#093}.fIP9ce{color:#c00}.LDBB9d{padding:1px}.gssb_a{padding:0 10px !important
}.gssb_c{left:132px !important;right:295px !important;top:78px !important;width:572px !important}.gssb_c table{font-size:16px !important}.gssb_e{border:1px solid #ccc !important;
border-top-color:#d9d9d9 !important}.gssb_i{background:#eee !important}#res{padding:0 8px}#rhs_block{padding-top:43px}#MCN7mf{padding:0 8px
}#subform_ctrl{font-size:11px;height:17px;margin:5px 3px 0 17px}.taf{padding-bottom:3px}.WIkLp{padding:20px 0 3px}.FuZzl{padding:20px 0 3px}#topstuff .e{padding-bottom:6px
}.slk .sld{width:250px}.slk{margin-bottom:-3px}.slk .zaHRAf{padding-bottom:5px;width:250px}.ac,.st{line-height:1.24}.a1DBFd,#ofr{font-size:16px;margin:1em 0;padding:0 8px
}.tZz6cc{padding-bottom:25px}.s{color:#545454}.ac{color:#545454}a.fl,.A8ul6 a,.osl a{color:#1a0dab;text-decoration:none}a:link{color:#1a0dab;cursor:pointer}#tads a:link{color:#1a0dab
}#tads .soc a:link{color:#808080}a:visited{color:#61C}.blg a{text-decoration:none}cite,cite a:link{color:#006621;font-style:normal}#tads cite{color:#006621}.hJND5c{font-size:15px
}.kvs{margin-top:1px}.hJND5c,.kvs,.slp{display:block;margin-bottom:1px}.kt{border-spacing:2px 0;margin-top:1px}.f{color:#808080}.L4Zeue{color:#093}h4.r{display:inline;font-size:small;
font-weight:normal}.g{line-height:1.2}.NpC9Hd{display:inline-block;vertical-align:top;overflow:hidden;position:relative}.COi8F{margin:0 0 2em 1.3em}.COi8F li{list-style-type:disc
}.osl{color:#777;margin-top:4px}.r{font-size:16px;margin:0}.gL9Hy{font-size:16px}.spell_orig{font-size:13px}.spell_orig a{text-decoration:none}.spell_orig b i{font-style:normal;
font-weight:normal}.th{border:1px solid #ebebeb}.ts td{padding:0
}.videobox{padding-bottom:3px}.slk a{text-decoration:none}#leftnav a:hover,#leftnav .tbou a:hover,.slk h3 a,a:hover{text-decoration:underline
}#mn{table-layout:fixed;width:100%}#leftnav a{color:#222;font-size:13px}#leftnav{padding:43px 4px 4px 0}.tbos{color:#dd4b39}.tbt{margin-bottom:28px}#tbd{padding:0 0 0 16px
}.tbou a{color:#222}#center_col{border:0;padding:0 8px 0 0}#topstuff .e{padding-top:3px}#topstuff .p64x9c{padding-top:6px}#ab_name{color:#dd4b39;font:20px "Arial";
margin-left:15px}#resultStats{color:#999;font-size:13px;overflow:hidden;white-space:nowrap}.mslg>td{padding-right:1px;padding-top:2px}.slk .sld{margin-top:2px;
padding:5px 0 5px 5px}.fmp{padding-top:3px}.close_btn{overflow:hidden}#fll a,#bfl a{color:#1a0dab !important;margin:0 12px;text-decoration:none !important}.ng{color:#dd4b39
}#mss{margin:.33em 0 0;padding:0;display:table}.NYKCib{display:inline-block;float:left;white-space:nowrap;padding-right:16px}#mss p{margin:0;padding-top:5px
}.tn{border-bottom:1px solid #ebebeb;display:block;float:left;height:59px;line-height:54px;min-width:980px;padding:0;position:relative;white-space:nowrap
}.qrSWbe,a.qrSWbe{color:#777;cursor:pointer;display:inline-block;font-family:arial,sans-serif;font-size:small;height:54px;line-height:54px;margin:0 8px;
padding:0 8px;text-decoration:none;white-space:nowrap}.tnuiC{border-bottom:3px solid #dd4b39;color:#dd4b39;font-weight:bold;margin:2px 8px 0}a.KDZjCd:hover{color:black;
text-decoration:none;white-space:nowrap}body{margin:0;padding:0}.sFTC8c{display:inline-block;float:left;margin-top:2px}.pqkqJe,a.pqkqJe{margin-left:1px}.sd{line-height:43px;
padding:0 8px 0 9px}a:active,.osl a:active,.tbou a:active,#leftnav a:active{color:#dd4b39}#bfl a:active{color:#dd4b39 !important}.csb{background:url(/images/nav_logo229.png) no-repeat;
overflow:hidden}.close_btn{background:url(/images/nav_logo229.png) no-repeat -138px -84px;height:14px;
width:14px;display:block}.star{background:url(/images/nav_logo229.png) no-repeat -94px -245px;height:13px;
width:65px;display:block}.star div,.star span{background:url(/images/nav_logo229.png) no-repeat 0 -245px;height:13px;
width:65px;display:block}.Pj9hGd{display:inline;margin:0 3px;outline-color:transparent;overflow:hidden;
position:relative}.Pj9hGd>div{outline-color:transparent}.CiacGf{border-color:transparent;
border-style:solid dashed dashed;border-top-color:green;border-width:4px 4px 0 4px;cursor:pointer;display:inline-block;
font-size:0;height:0;left:4px;line-height:0;outline-color:transparent;position:relative;top:-3px;width:0}.CiacGf{margin-top:-4px}.am-dropdown-menu{display:block;background:#fff;
border:1px solid #dcdcdc;font-size:13px;left:0;padding:0;position:absolute;right:auto;white-space:nowrap;
z-index:3}.mUpfKd{list-style:none;white-space:nowrap}.mUpfKd:hover{background-color:#eee}a.imx0m{color:#333;cursor:pointer;
display:block;padding:7px 18px;text-decoration:none}#tads a.imx0m{color:#333}.sfbgg{background:#f1f1f1;
border-bottom:1px solid #e5e5e5;height:71px}#logocont{z-index:1;padding-left:4px;padding-top:4px
}#logo{display:block;height:49px;
margin-top:12px;margin-left:12px;overflow:hidden;position:relative;width:137px}#logo img{left:0;position:absolute;
top:-41px}.lst-a{background:white;border:1px solid #d9d9d9;border-top-color:silver;width:570px}.lst-a:hover{border:1px solid #b9b9b9;
border-top:1px solid #a0a0a0;box-shadow:inset 0 1px 2px rgba(0,0,0,0.1);-webkit-box-shadow:inset 0
1px 2px rgba(0,0,0,0.1);
-moz-box-shadow:inset 0 1px 2px rgba(0,0,0,0.1)}.lst-td{border:none;padding:0}.tia input{border-right:none;
padding-right:0}.tia{padding-right:0}.lst{background:none;border:none;color:#000;font:16px arial,sans-serif;
float:left;height:22px;margin:0;padding:3px 6px 2px 9px;vertical-align:top;width:100%;
word-break:break-all}.lst:focus{outline:none}.lst-b{background:none;
border:none;height:26px;padding:0 6px 0 12px}.ds{border-right:1px solid #e7e7e7;position:relative;
height:29px;margin-left:17px;z-index:100}.lsbb{background-image:-moz-linear-gradient(top,#4d90fe,#4787ed);
background-image:-ms-linear-gradient(top,#4d90fe,#4787ed);background-image:-o-linear-gradient(top,#4d90fe,#4787ed);
background-image:-webkit-gradient(linear,left top,left bottom,from(#4d90fe),to(#4787ed));
background-image:-webkit-linear-gradient(top,#4d90fe,#4787ed);background-image:linear-gradient(top,#4d90fe,#4787ed);
border:1px solid #3079ed;border-radius:2px;
background-color:#4d90fe;height:27px;width:68px}.lsbb:hover{background-image:-moz-linear-gradient(top,#4d90fe,#357ae8);
background-image:-ms-linear-gradient(top,#4d90fe,#357ae8);background-image:-o-linear-gradient(top,#4d90fe,#357ae8);
background-image:-webkit-gradient(linear,left top,left bottom,from(#4d90fe),to(#357ae8));
background-image:-webkit-linear-gradient(top,#4d90fe,#357ae8);background-color:#357ae8;
background-image:linear-gradient(top,#4d90fe,#357ae8);border:1px solid #2f5bb7}.lsb{background:transparent;
background-position:0 -343px;
background-repeat:repeat-x;border:none;
color:#000;cursor:default;font:15px arial,sans-serif;
height:29px;margin:0;vertical-align:top;
width:100%}.lsb:active{-moz-box-shadow:inset 0 1px 2px rgba(0,0,0,0.3);-webkit-box-shadow:inset 0 1px 2px rgba(0,0,0,0.3);
box-shadow:inset 0 1px 2px rgba(0,0,0,0.3);
background:transparent;color:transparent;overflow:hidden;position:relative;width:100%}.sbico{color:transparent;
display:inline-block;height:15px;margin:0 auto;margin-top:2px;
width:15px;overflow:hidden}</style>
<script nonce="cIrvPG0MvCAr3nWe2roe/g==">
(function(){window.google={
kEI:'16NHXKPaGOKU0gKPk6KACw',kEXPI:'0,18168,1335579,57,1958,1016,1406,698,527,730,326,1123,350,30,1227,806,89,242,662,2335336,159,32,68,318922,10304,1294,12383,
4855,32692,15247,867,7505,3256,1402,5281,1100,3335,2,2,4605,2196,364,529,636,7,7652,224,1017,1195,
5373,575,835,284,2,1306,2432,58,2,1,3,1297,4325,3388,8,302,1268,773,2249,1408,3337,1146,5,
2,2,1749,214,2595,182,283,3136,669,1050,464,1344,386,743,268,81,7,1,2,25,463,620,29,983,
6,406,458,1847,769,536,696,3394,1209,878,410,2,554,1604,949,81,381,286,152,157,639,1220,
38,363,557,573,145,155,499,718,42,51,864,339,68,484,47,590,295,195,1284,1085,367,802,
8,2,247,499,1245,227,31,2,366,265,217,942,1215,188,2,4,2,670,44,218,116,1424,10,11,408,
349,167,82,247,879,373,804,221,580,54,293,606,11,537,12,620,446,18,87,300,247,
316,44,227,79,25,440,116,91,87,361,20,317,255,2,83,340,102,495,1,696,3,1032,192,10,
1,2,871,28,135,7,10,4,176,76,85,266,243,506,86,426,537,35,612,19,5965997,13,2541,121,
114,20,5997346,90,25116827',
authuser:0,kscs:'c9c918f0_16NHXKPaGOKU0gKPk6KACw',kGL:'US'};
google.kHL='en';})();google.time=function(){return(new Date).getTime()};
(function(){google.lc=[];google.li=0;google.getEI=function(a){
for(var b;a&&(!a.getAttribute||!(b=a.getAttribute("eid")));
)a=a.parentNode;return b||google.kEI};google.getLEI=function(a){
for(var b=null;a&&(!a.getAttribute||!(b=a.getAttribute("leid")));
)a=a.parentNode;return b};
google.https=function(){return"https:"==window.location.protocol};
google.ml=function(){return null};
google.log=function(a,b,e,c,g){if(a=google.logUrl(a,b,e,c,g)){
b=new Image;var d=google.lc,f=google.li;
d[f]=b;b.onerror=b.onload=b.onabort=function(){delete d[f]};
google.vel&&google.vel.lu&&google.vel.lu(a);
b.src=a;google.li=f+1}};google.logUrl=function(a,b,e,c,g){var d="",f=google.ls||"";
e||-1!=b.search("&ei=")||(d="&ei="+google.getEI(c),-1==b.search("&lei=")&&(c=google.getLEI(c))&&(d+="&lei="+c));
c="";!e&&google.cshid&&-1==b.search("&cshid=")&&"slh"!=a&&(c="&cshid="+
google.cshid);a=e||"/"+(g||"gen_204")+"?atyp=i&ct="+a+"&cad="+b+d+f+"&
zx="+google.time()+c;
/^http:/i.test(a)&&google.https()&&(google.ml(Error("a"),!1,{src:a,glmm:1
}),a="");return a};
}).call(this);(function(){google.y={};
google.x=function(a,b){
if(a)var c=a.id;
else{do c=Math.random();while(google.y[c])}
google.y[c]=[a,b];
return!1};google.lm=[];
google.plm=function(a){google.lm.push.apply(google.lm,a)};
google.lq=[];
google.load=function(a,b,c){google.lq.push([[a],b,c])};
google.loadAll=function(a,b){google.lq.push([a,b])};
}).call(this);google.f={};
(function(){var b={gen204:"dcl",clearcut:4};
var c=[function(){google.c&&google.tick("load",b)}];
google.dclc=function(a){c.length?c.push(a):a()};
function d(){for(var a;
a=c.shift();
)a()}window.addEventListener?(document.addEventListener("DOMContentLoaded",d,!1),window.addEventListener("load",d,!1)):window.attachEvent&&
window.attachEvent("onload",d);
}).call(this);
</script>
<script type="text/javascript" nonce="cIrvPG0MvCAr3nWe2roe/g==">
</script>
<script nonce="cIrvPG0MvCAr3nWe2roe/g==">
(function(){google.sham=function(c){for(var d=c.parentElement,a=null,b=0;
b<d.childNodes.length;b++){
var e=d.childNodes[b];
-1<(" "+e.className+" ").indexOf(" am-dropdown-menu ")&&(a=e)
}
"none"==a.style.display?(a.style.display="",google.log("hpam","&ved="+c.getAttribute("data-ved"))):a.style.display="none"};
}).call(this);
(function(){var b=[];google.jsc={xx:b,x:function(a){
b.push(a)},mm:[],m:function(a){google.jsc.mm.length||(google.jsc.mm=a)}
};}).call(this);</script></head>
<body class="hsrp" bgcolor="#ffffff" marginheight="0" marginwidth="0" topmargin="0"><div id=gbar><nobr>
<b class=gb1>Search</b>
 <a class=gb1 href="https://www.google.com/search?hl=en&tbm=isch&source=og&tab=wi">Images</a>
 <a class=gb1 href="https://maps.google.com/maps?hl=en&tab=wl">Maps</a>
 <a class=gb1 href="https://play.google.com/?hl=en&tab=w8">Play</a>
 <a class=gb1 href="https://www.youtube.com/results?gl=US&tab=w1">YouTube</a>
 <a class=gb1 href="https://news.google.com/nwshp?hl=en&tab=wn">News</a>
 <a class=gb1 href="https://mail.google.com/mail/?tab=wm">Gmail</a>
 <a class=gb1 href="https://drive.google.com/?tab=wo">Drive</a>
 <a class=gb1 style="text-decoration:none" href="https://www.google.com/intl/en/about/products?tab=wh"><u>More</u> &raquo;</a>
</nobr>
</div><div id=guser width=100%><nobr>
<span id=gbn class=gbi></span><span id=gbf class=gbf></span>
<span id=gbe></span><a href="http://www.google.com/history/optout?hl=en" class=gb4>Web History</a> |
 <a  href="/preferences?hl=en" class=gb4>Settings</a> |
 <a target=_top id=gb_70 href=
 "https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/search%3Fq%3Dcars%26oq%3Dcars%26hl%3Den%26gl%3Dus%26sourceid%3Dchrome%26ie%3DUTF-8"
 class=gb4>Sign in</a></nobr>
</div><div class=gbh style=left:0></div><div class=gbh style=right:0></div><table id="mn" border="0" cellpadding="0" cellspacing="0" style="position:relative">
<tr><th width="132"></th>
<th width="573"></th>
<th width="278"></th>
<th></th></tr><tr>
<td class="sfbgg" valign="top">
<div id="logocont"><h1><a href="/webhp?hl=en" style="background-image:url(/images/nav_logo229.png);
background-repeat:no-repeat;height:37px;
width:95px;display:block;
background-position:0 -41px" id="logo" title="Go to Google Home"></a></h1>
</div></td>
<td class="sfbgg" colspan="2" valign="top" style="padding-left:0px">
<form style="display:block;margin:0;background:none" action="/search" id="tsf" method="GET" name="gs">
<table border="0" cellpadding="0" cellspacing="0" style="margin-top:20px;
position:relative">
<tr><td>
<div class="lst-a">
<table cellpadding="0" cellspacing="0"><tr>
<td class="lst-td" width="555" valign="bottom">
<div style="position:relative;zoom:1"><input class="lst" value="cars" title="Search" autocomplete="off" id="sbhost" maxlength="2048" name="q" type="text"></div></td></tr>
</table></div></td>
<td><div class="ds"><div class="lsbb"><button class="lsb" value="Search" name="btnG" type="submit">
<span class="sbico" style="background-image:url(/images/nav_logo229.png);background-repeat:no-repeat;
height:14px;width:13px;display:block;
background-position:-36px -111px"></span>
</button></div></div></td></tr></table><input name="hl" value="en" type="hidden"><input name="gl" value="us" type="hidden">
</form></td><td class="sfbgg">&nbsp;</td>
</tr><tr style="position:relative"><td>
<div style="border-bottom:1px solid #ebebeb;height:59px"></div></td>
<td colspan="2"><div class="tn"><div class="qrSWbe tnuiC sFTC8c pqkqJe">All</div>
<div class="sFTC8c">
<a class="qrSWbe KDZjCd" href="/search?q=cars&amp;hl=en&amp;gl=us&amp;ie=UTF-8&amp;prmd=ivns&amp;source=lnms&amp;tbm=isch&amp;sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQ_AUIBQ">Images</a>
</div><div class="sFTC8c"><a class="qrSWbe KDZjCd"
href="/search?q=cars&amp;hl=en&amp;gl=us&amp;ie=UTF-8&amp;prmd=ivns&amp;source=lnms&amp;tbm=vid&amp;sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQ_AUIBg">Videos</a>i
</div><div class="sFTC8c"><a class="qrSWbe KDZjCd"
href="/search?q=cars&amp;hl=en&amp;gl=us&amp;ie=UTF-8&amp;prmd=ivns&amp;source=lnms&amp;tbm=nws&amp;sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQ_AUIBw">News</a>i
</div><div class="sFTC8c"><a class="qrSWbe KDZjCd"
href="/search?q=cars&amp;hl=en&amp;gl=us&amp;ie=UTF-8&amp;prmd=ivns&amp;source=lnms&amp;tbm=shop&amp;sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQ_AUICA">Shopping</a>i
</div><div class="sFTC8c"><a class="qrSWbe KDZjCd"
href="https://maps.google.com/maps?q=cars&amp;hl=en&amp;gl=us&amp;um=1&amp;ie=UTF-8&amp;sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQ_AUICQ">Maps</a>i
</div><div class="sFTC8c"><a class="qrSWbe KDZjCd" href=
"/search?q=cars&amp;hl=en&amp;gl=us&amp;ie=UTF-8&amp;prmd=ivns&amp;source=lnms&amp;tbm=bks&amp;sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQ_AUICg">Books</a>
</div></div><div style="border-bottom:1px solid #ebebeb;height:59px">
</div></td><td>
<div style="border-bottom:1px solid #ebebeb;height:59px"></div></td></tr>
<tbody id="desktop-search"><style>.pCA4Bd,.pCA4Bd a:link,.pCA4Bd a:visited,a.pCA4Bd:link,a.pCA4Bd:visited{color:#808080
                                                                                                         }.AzrInc{color:#61C}.ellip{overflow:hidden;
                                                                                                                  text-overflow:ellipsis;
                                                                                                                  white-space:nowrap}.dg4MBd
img{border-top-left-radius:2px;border-top-right-radius:2px}.WPcjGf .dg4MBd
img{border-top-left-radius:0i
   }.rllt__wrapped,.rllt__wrap-on-expand{}.rllt__wrapped,.rllt__details
.rllt__wrapped,.rllt__details .rllt__wrapped div{white-space:normal;
 }.rl-qs-crs-t .rllt__details .rllt__wrap-on-expand{white-space:nowrap
 }.rllt__details .rllt__wrap-on-expand,.tile-static .rllt__details .rllt__wrap-on-expand{white-space:normal
 }.rllt__details .rllt__wrap-on-expand div{white-space:inherit;overflow:inherit;
 text-overflow:inherit}.kR1eme{color:rgba(0,0,0,.87);font-size:16px;
 line-height:18px;
 }.t1IUkc{display:flex}.mQiB1{display:inline-block;float:none;
 vertical-align:-1px;
 }.BTtC6e{color:#e7711b}.VY7aBe{margin:0 4px}.EIKTG{color:#cc4125}.orNyrb{color:#f09300}.LiTCwd{color:#66667d
 }.rl-qs-crs-t .rllt__multi-line>:not(:first-child){display:none
 }.rl-qs-crs-t .rllt__initially-hidden{display:none
 }.MmpQZb{background:url(data:image/png;base64,
 iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAATUlEQVR4AWPwySykKR61AIJHLZDiXd0AwtS1AGF4IBD/g+IGciygqSUggqaWgAiaWgIiKLJkKFmAafhQiWRMw+md0Qa+qKAMj1owagEA9oqlMViMbnkAAAAASUVORK5CYII=)}
 .boLwW{display:inline-block;
 height:18px;width:18px}.nap1td,.nap1td:link,.nap1td:visited{color:#1a0dab;
 display:table-cell;font-size:11px;line-height:20px;text-align:center;
 text-decoration:none;text-transform:uppercase;vertical-align:middle;
 width:54px}.nap1td:last-child{width:94px}.hc8x7b{text-align:center;
 width:104px}.LPMtqb,.LPMtqb:hover,.LPMtqb:link,.LPMtqb:visited{color:#757575;
 font-size:14px;text-decoration:none}#rcnt a.LPMtqb,#rcnt a.LPMtqb:hover,#rcnt a.LPMtqb:link,#rcnt a.LPMtqb:visited{
 text-decoration:none}.IvtMPc{border-bottom:1px solid #ebebeb;padding:11px 0 11px 16px;text-align:left}.IvtMPc:last-child{border:none}.O6u2Ve{border-collapse:collapse;table-layout:fixed;
 width:100%}.O6u2Ve td{padding:0}.elzrQ{color:#1a0dab;display:block;
 padding:14px 16px}.elzrQ{font-size:16px}.elzrQ:hover{text-decoration:underline
 }.ksBKIe{border:1px solid #ebebeb;
 overflow:hidden}.VBt9Dc{border:1px solid #e0e0e0;font-size:13px;
 margin-right:-2px;}.V7Q8V{margin:4px 10px}.AwJT2c{background:white;
 border-bottom:0;border-left:0;border-right:0;border-top:1px solid #e0e0e0;cursor:pointer;
 height:40px;outline:0;width:100%}.dxrUgb{color:#777;font-size:11px}.dxrUgb a{color:#777;
 text-decoration:none}.xpdclpsbtn{}.xpdxpndbtn{}.xpdclpsbtn .KMK5T{background:url(/images/nav_logo229.png
 ) no-repeat -50px -79px;
 height:22px;width:64px}.xpdxpndbtn .KMK5T{
 background:url(/images/nav_logo229.png) no-repeat -50px -102px;
 height:22px;width:64px}.mraOPb{color:#222;font-size:15px;
 line-height:normal;margin:12px 0}.dXAUyb{margin:4px 0}.R8KuR{margin:10px;overflow:hidden;
 position:relative;white-space:nowrap;}.M1e9Oe{display:-moz-inline-stack;
 display:inline-block;position:relative;
 width:100%;z-index:0;}.OSMzvb{display:-moz-inline-stack;
 display:inline-block;max-width:100%;
 overflow:hidden;
 }.JKXCdf{position:absolute;right:0;z-index:1;
 }.FSP1Dd{border-top:1px solid #e0e0e0;color:#000;font-size:22px;
 margin-top:-5px;padding-top:10px}.CB9G1b{color:#000;
 font-size:14px}.F7uZG{color:#777;
 margin:4px 0;overflow:hidden}.Rlw09{margin-bottom:20px}.cC4Myd{color:#212121}.A1t5ne{color:#777
 }.cC4Myd{font-weight:bold}.xKoZHf{margin-left:10px
 }.B27ELd.ty7XEe{margin-right:10px}.x32fhf{color:#222;font-size:18px;
 margin:20px 0 8px 0}.lHETUb{color:#222;
 font-size:18px;margin:20px 10px 8px 10px}.B27ELd{display:-moz-inline-stack;
 display:inline-block;margin-bottom:10px;margin-right:21px;
 text-align:left;vertical-align:top;
 }.tQOFN{overflow:hidden}.czonVc{color:#777;overflow:hidden;
 text-overflow:ellipsis;white-space:normal;
 word-wrap:break-word}.brYqc{margin:6px 0 0 8px;overflow:hidden;
 text-overflow:ellipsis;white-space:normal;
 word-wrap:break-word}.u6RhQc{margin:4px 10px
 }#k2fPW{border:1px solid #e0e0e0;font-size:13px;
 margin-right:-2px;}.C6ZAab{color:#000}.NWncrd{border-spacing:0;
 line-height:20px;table-layout:fixed;
 width:100%}.NWncrd a:hover,.NWncrd a:active{text-decoration:none
 }.JYQZge{color:#1a0dab}a:hover .JYQZge,a:active .JYQZge{
 text-decoration:underline}.TyXs8d{border-top:1px solid #e0e0e0;
 margin:0 -10px;padding:0 10px}.DBHfJe{display:block;
 margin:auto}.rNjNwd{padding-top:8px;
 padding-bottom:8px}.vrQIef{max-width:198px;overflow:hidden;
 text-overflow:ellipsis;white-space:nowrap}
 </style><tr><td id="leftnav" valign="top">
 <div><h2 class="hd">Search Options</h2>
 <ul class="med" id="tbd"><li>
 <ul class="tbt"><li class="tbos" id="qdr_">Any time</li>
 <li class="tbou" id="qdr_h"><a class="q" href=
 "/search?q=cars&amp;hl=en&amp;gl=us&amp;ie=UTF-8&amp;prmd=ivns&amp;source=lnt&amp;tbs=qdr:h&amp;sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQpwUIDw">Past hour</a>
 </li><li class="tbou" id="qdr_d"><a class="q" href=
 "/search?q=cars&amp;hl=en&amp;gl=us&amp;ie=UTF-8&amp;prmd=ivns&amp;source=lnt&amp;tbs=qdr:d&amp;sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQpwUIDw">Past 24 hours</a>
 </li><li class="tbou" id="qdr_w">
 <a class="q" href="/search?q=cars&amp;hl=en&amp;gl=us&amp;ie=UTF-8&amp;prmd=ivns&amp;source=lnt&amp;tbs=qdr:w&amp;sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQpwUIDw">Past week</a>
 </li><li class="tbou" id="qdr_m">
 <a class="q" href="/search?q=cars&amp;hl=en&amp;gl=us&amp;ie=UTF-8&amp;prmd=ivns&amp;source=lnt&amp;tbs=qdr:m&amp;sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQpwUIDw">Past month</a>
 </li><li class="tbou" id="qdr_y">
 <a class="q" href="/search?q=cars&amp;hl=en&amp;gl=us&amp;ie=UTF-8&amp;prmd=ivns&amp;source=lnt&amp;tbs=qdr:y&amp;sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQpwUIDw">Past year</a>
 </li></ul></li><li><ul class="tbt">
 <li class="tbos" id="li_">All results</li>
 <li class="tbou" id="li_1">
 <a class="q" href="/search?q=cars&amp;hl=en&amp;gl=us&amp;ie=UTF-8&amp;prmd=ivns&amp;source=lnt&amp;tbs=li:1&amp;sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQpwUIDw">Verbatim</a>
 </li></ul></li></ul></div></td>
 <td valign="top"><div id="center_col">
 <div class="sd" id="resultStats">About 11,810,000,000 results</div>
 <div id="res"><div id="topstuff"></div>
 <div id="search"><div id="ires"><ol><div class="g"><h3 class="r">
 <a href="/url?q=https://www.cars.com/&amp;sa=U&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQFggVMAA&amp;usg=AOvVaw26LGci4jL3CMDlKzFU-n4V"
 >New <b>Cars</b>, Used <b>Cars</b>, <b>Car</b> Reviews and News | <b>Cars</b>.com</a>
 </h3><div class="s"><div class="hJND5c" style="margin-bottom:2px">
 <cite>https://www.<b>cars</b>.com/</cite><div class="Pj9hGd"><div style="display:inline"
 onclick="google.sham(this);" aria-expanded="false" aria-haspopup="true" tabindex="0"
 data-ved="0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQ7B0IFjAA">
 <span class="CiacGf"></span></div>
 <div style="display:none" class="am-dropdown-menu" role="menu" tabindex="-1">
 <ul>
 <li class="mUpfKd"><a class="imx0m" href=
 "/url?q=http://webcache.googleusercontent.com/search%3Fq%3Dcache:dHqrANYaU_oJ:https://www.cars.com/%252Bcars%26hl%3Den%26gl%3Dus%26ct%3Dclnk&amp;sa=U&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQIAgYMAA&amp;usg=AOvVaw3IfK277B707SbEESCwa6CG">Cached</a>
 </li><li class="mUpfKd">
 <a class="imx0m" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=related:https://www.cars.com/+cars&amp;tbo=1&amp;sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQHwgZMAA">Similar</a>
 </li></ul></div></div></div>
<span class="st">Research and compare <b>cars</b>, find local dealers/sellers, calculate loan payments, <br>
find your <b>car&#39;s</b> value, sell or trade your <b>car</b>, get a service estimate, and much&nbsp;...</span><br>
</div><table class="slk" style="border-collapse:collapse;margin-top:1px" cellpadding="0" cellspacing="0">
<tr class="mslg"><td style="padding-left:23px;vertical-align:top"><div class="sld"><h3 class="r"><a class="sla" href=
"/url?q=https://www.cars.com/shopping/&amp;sa=U&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQjBAIHDAB&amp;usg=AOvVaw1H0w2_Dx71RHvzC6sg6mTA">Cars for Sale</a></h3><div class=
"s st" style="width:220px;overflow:hidden">Browse cars for sale on Cars.com. Shop the best deals near you ...</div>
</div></td><td style="padding-left:7px;vertical-align:top"><div class="sld"><h3 class="r"><a class="sla" href="/url?
q=https://www.cars.com/sell/&amp;sa=U&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQjBAIHjAD&amp;
usg=AOvVaw3kum0T5KsjsVQ0mUYF5K13">Sell Your Car</a></h3><div class="s st" style="width:220px;overflow:hidden">
Get offers from dealers and sell your car fast with Quick Offer ...</div></div></td></tr>
<tr class="mslg"><td style="padding-left:23px;vertical-align:top"><div class="sld"><h3 class="r"><a class="sla" href=
"/url?q=https://www.cars.com/for-sale/advanced-search/&amp;sa=U&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQjBAIIDAC&amp;usg=AOvVaw2_flJ4kW-fPAljDNsYusc1">Advanced Search</a></h3><div class=
"s st" style="width:220px;overflow:hidden">Advanced search allows you to filter 4.9 million new &amp; used cars ...
</div></div></td><td style="padding-left:7px;vertical-align:top"><div class="sld"><h3 class="r"><a class="sla" href=
"/url?q=https://www.cars.com/research/&amp;sa=U&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQjBAIIjAE&amp;
usg=AOvVaw22pkmvIKx6wSMtgBLA0kFF">Research</a></h3><div class="s st" style="width:220px;overflow:hidden">Start your re
search for your next car by comparing popular ...</div></div></td></tr><tr><td colspan="2" style="padding-left:28px;
vertical-align:top"><div style="padding-top:5px"><a class="fl" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=+site:
cars.com+cars&amp;sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQrAMIIw">More results from cars.com </a></div></td></tr>
</table></div><div class="g"><div><h3 class="r"><a href="/search?q=cars&amp;hl=en&amp;gl=us&amp;ie=UTF-8&amp;
prmd=ivns&amp;source=univ&amp;tbm=nws&amp;tbo=u&amp;sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQqAIIJQ">News for <b>
cars</b></a></h3><table class="ts"><tr><td valign="top" style="font-size:78%;line-height:normal;padding:7px 8px 0 0;
text-align:center"><a href="/url?q=https://jalopnik.com/here-are-some-of-the-most-ridiculous-custom-cars-rolls-18
31955418&amp;sa=U&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQpwIIJg&amp;usg=AOvVaw0iQQNteqH_sM3EWEu1lvnQ"><img class=
"th" height="100" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvhOhFT4GXFT5ZUFEjOC_VHrFoO2KviNc0i3ju2W_b
zuqfcPxy3USdQuxfxicJiVQqDQ" width="100" border="1"><br></a><span class="L4Zeue ybhkme">Jalopnik</span></td><td valign=
"top"><div style="margin-top:5px"><a href="/url?q=https://jalopnik.com/here-are-some-of-the-most-ridiculous-custom-car
s-rolls-1831955418&amp;sa=U&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQqQIIKDAF&amp;usg=AOvVaw0xLyxDbYuJyQwxJrpShWb2">
Here Are Some of the Most Ridiculous Custom Cars Rolls-Royce Built Last Year</a><div style="padding-top:2px"><cite>
Jalopnik</cite><span class="f"> - <span class="nobr">2 hours ago</span><span class="nobr"></span></span></div>
<div class="j" style="margin-top:1px;margin-bottom:4px"><span class="st">Some of the <b>cars</b> belong to collections
, like the Silver Ghost Collection that the <br>
company made to &#8220;pay homage&#8221; to the original Silver Ghost from&nbsp;...</span></div></div><div style=
"margin-top:4px"><a href="/url?q=https://6abc.com/fire-and-ice-firefighting-efforts-leave-ice-covered-cars-roads-/
5099831/&amp;sa=U&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQqQIIKjAG&amp;usg=AOvVaw3x25_mRfhABTJF3mzwxfsk">Fire &amp;
 Ice: Firefighting efforts cover streets, cars in ice across Philadelphia region</a><div style="padding-top:2px"><cite>
WPVI-TV</cite><span class="f"> - <span class="nobr">12 hours ago</span><span class="nobr"></span></span></div></div>
<div style="margin-top:4px"><a href="/url?q=https://jalopnik.com/driving-a-1970-triumph-gt6-reminds-you-cars-once-had
-s-1831472182&amp;sa=U&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQqQIILDAH&amp;usg=AOvVaw3DrmfBvViudviWedfg9LNX">Driving a 1970 Triumph GT6+ Re
minds You Cars Once Had Steep Learning Curves</a><div style="padding-top:2px"><cite>Jalopnik</cite><span class=
"f"> - <span class="nobr">5 hours ago</span><span class="nobr"></span></span></div></div></td></tr></table></div></div>
<div class="ksBKIe g"><a href="https://maps.google.com/maps?hl=en&amp;gl=us&amp;um=1&amp;ie=UTF-8&amp;fb=1&amp;sa=X
&amp;sll=41.273344,-73.082028&amp;sspn=0.099089,0.1757967&amp;q=cars&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQtgMIMg
" style="cursor:pointer;position:relative;height:200px;display:block" tabindex="0"><img height="200" id="lu_map" src=
"/maps/vt/data=0k9veMBSCEvRPHWLFs43rwP4qCJpZNJ_HxfT2aX70uHOk_tZnaQm5_Bcv9Und1FA2c5tbWc-hD-fB-cWeZmi98ptf2RX7kVfbl1JCo
YeOi-oRbHc6Wko1aiAIWTWHoxWepy063FgRS9asHo8SiRKC8m6bCr620e_97baMIOqF3yrLu2nVzTP3Vm9abacWIWQ6FWZZOEk5Do5vf57FjFWls52HwZ
CrdLpeoKkhcYjosAcdKkeFGoGZAs4G3Whlsg7qIyOxjbeneOnM6zqA8rHRy9wIrO7yXXU7GgGmO9bG8-cCdBNj67jJjHEWohT3ZmpJAbW5Ek8iiYv9
GoZ5WpMKUQx7XrFpS_edh2yGMgnWJz2ywLcIV1X2v7NItsqzyBnKKztXOLMSeAbka_lRsezNATNtBbZFwoms_53vVqOLBvOlKjQD8glPLactgDiPSnZ00
zIbP4NEjsTZgEJ3OJoozAQIBqAjon3v9ZSftijPr07OAnBGf_8E7agYa51EDoFmkCWdJktvs74K7IkfFF7iabSgNtPeQpG2byposKzr0KGNoguyeFYaqJZ
19CDafOdGvRwDhPCqDx5PG3_lojHbDiDdlM3FXSf8w2Ctgw3begaql1wbGD4fqL6EbDkLL1islzTjbrhEHk5JIyOR3gC7O2sAi_XepwHn7vmi4nwGQDuB5
-olfUqVS-dwGPkQ6E_QxKQSoTdyV3QlCXMnBsiYhekTBd-SMDkBgJa_ZjnmSR6UaSFANsNLp4XcVKMikl0WrzZe8JmkEVjpEbS9I8j9lVcHeGIHfOkGeR
pNFY_7mDzduX195A4QpBy8TmGGiwvfOvUuLYDvSnvdD6QEjPs0Z3_AE8dxdKvBCHzWAdYQxnBchk0Bkc6XYdU3VwF_82mGI8vYRaOSjUcWuBZh44O54Np
f3v1WHA63VaKInbcmvLeJIYG7Pb-EPk_bv7_kszaqLo_oAELb73_h9sGkjSlB93TcG506pjAe9qfHAmySk0e7fzzV3hshemxZgnMI63mtQ0KZFcTG-9z
FMDi4zZOgmucziw7ZzJgjm6hKY0ciqBJcOQCFRMcRUWuew" width="547" title="Map of cars" alt="Map of cars" border="0"></a>
<div class="IvtMPc"><table class="O6u2Ve"><td><a class="LPMtqb" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=Center
+Motor+Sports+Shelton,+CT&amp;ludocid=13380871646143602238&amp;sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQvS4INTAI">
<div class="kR1eme gsrt rllt__wrap-on-expand" aria-level="3" role="heading"><span>Center Motor Sports</span></div><div>
<span class="BTtC6e">4.7</span> <g-review-stars><div class="mQiB1 star"><div style="width:59px">&nbsp;</div></div>
</g-review-stars> (13) &middot; Used car dealer</div><div><span>Shelton, CT</span> &middot; (203) 513-2072</div><div>
<div class="rllt__wrapped EIKTG">Closed now</div></div></a></td><td class="hc8x7b"><a href="/search?hl=en&amp;
gl=us&amp;ie=UTF-8&amp;q=Center+Motor+Sports+Shelton,+CT&amp;ludocid=13380871646143602238&amp;sa=X&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQ_pABCDswCA" class="nap1td"><div class="boLwW MmpQZb"></div><div>More info</div>
</a></td></table></div><div class="IvtMPc"><table class="O6u2Ve"><td><a class="LPMtqb" href="/search?hl=en&amp;
gl=us&amp;ie=UTF-8&amp;q=Raro+Motor+Car,+LLC+Derby,+CT&amp;ludocid=3535410694801911484&amp;sa=X&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQvS4IPTAJ"><div class="kR1eme gsrt rllt__wrap-on-expand" aria-level="3" role=
"heading"><span>Raro Motor Car, LLC</span></div><div><span class="BTtC6e">4.3</span> <g-review-stars><div class=
"mQiB1 star"><div style="width:59px">&nbsp;</div></div></g-review-stars> (6) &middot; Used car dealer</div><div><span>
Derby, CT</span> &middot; (203) 735-1849</div><div><div class="rllt__wrapped EIKTG">Closed now</div></div></a></td>
<td class="hc8x7b"><a href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=Raro+Motor+Car,+LLC+Derby,+CT&amp;
ludocid=3535410694801911484&amp;sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQ_pABCEMwCQ" class="nap1td">
<div class="boLwW MmpQZb"></div><div>More info</div></a></td></table></div><div class="IvtMPc"><table class="O6u2Ve">
<td><a class="LPMtqb" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=car+mart+Milford,+CT&amp;
ludocid=14459009982927127753&amp;sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQvS4IRTAK"><div class=
"kR1eme gsrt rllt__wrap-on-expand" aria-level="3" role="heading"><span>car mart</span></div><div><span class="BTtC6e">
4.6</span> <g-review-stars><div class="mQiB1 star"><div style="width:59px">&nbsp;</div></div></g-review-stars>
 (10) &middot; <span>$</span> &middot; Used car dealer</div><div><span>Milford, CT</span> &middot; (203) 693-2900</div>
 <div><div class="rllt__wrapped EIKTG">Closed now</div></div></a></td><td class="hc8x7b"><a href="/search?hl=en&amp;
 gl=us&amp;ie=UTF-8&amp;q=car+mart+Milford,+CT&amp;ludocid=14459009982927127753&amp;sa=X&amp;
 ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQ_pABCEwwCg" class="nap1td"><div class="boLwW MmpQZb"></div><div>More info</div>
 </a></td></table></div><div><a class="elzrQ" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=cars&amp;npsic=0&amp;
 rlst=f&amp;rlha=0&amp;rllag=41273344,-73082028,5359&amp;sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQjGoITQ">
 More places</a></div></div><div class="g"><h3 class="r"><a href="/search?q=cars&amp;hl=en&amp;gl=us&amp;ie=UTF-8&amp;
 prmd=ivns&amp;tbm=isch&amp;tbo=u&amp;source=univ&amp;sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQsAQITw">
Images for <b>cars</b></a></h3><br><div><a href="/url?q=https://www.imdb.com/title/tt0317219/&amp;sa=U&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQwW4IUTAL&amp;usg=AOvVaw0awLT-PA8VJpA0jpMxSrjS"><img style="margin:3px 0;
margin-right:6px;padding:0" height="73" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:
ANd9GcTSaVCz9GjEPJLx0qm2mOa-yPr7CZRrpT8fkWgRNjRTseaLoDjFE6X0gIo" title="https://www.imdb.com/title/tt0317219/" width=
"130" alt="Image result for cars" align="middle"></a><a href="/url?q=https://cars.disney.com/&amp;sa=U&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQwW4IUzAM&amp;
usg=AOvVaw091EdPAUhDaqLsHGOGFeDo"><img style="margin:3px 0;margin-right:6px;padding:0" height="39" src=
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSuzvCLfKq8kPmfJeuLewZDH56VcZfDBH2SoZv7fyFUYtq8FK7EGDDSUWE
" title="https://cars.disney.com/" width="115" alt="Image result for cars" align="middle"></a><a href="/url?q=https:
//www.cars.com/shopping/&amp;sa=U&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQwW4IVTAN&amp;
usg=AOvVaw11VeoF1SFgn6LUhqTyqC3P"><img style="margin:3px 0;margin-right:6px;padding:0" height="88" src=
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQy1IYZIyhUEO8tE3Ycrgg5mt8hxPIdOgmuHGxRub_ckLZGk1DZhsw7gLUu
" title="https://www.cars.com/shopping/" width="133" alt="Image result for cars" align="middle"></a><a href="/url?q=
https://www.car.com/&amp;sa=U&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQwW4IVzAO&amp;usg=AOvVaw2obZWzeSaUADnhu3KLpPd2">
<img style="margin:3px 0;margin-right:6px;padding:0" height="90" src="https://encrypted-tbn0.gstatic.com/images?q=
tbn:ANd9GcQFDpMSzvn_VSsCPTW9--G_bueLt7y2YN3LLu8ELBTfo3XEuj75GsJ-wRDE" title="https://www.car.com/" width="135" alt=
"Image result for cars" align="middle"></a></div></div><div class="g"><h3 class="r"><a href="/url?q=https
://www.carmax.com/cars&amp;sa=U&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQFghZMA8&amp;usg=AOvVaw0zKuzP3bHSV2GveeOtewQa">Used <b>Cars</b> for Sale - CarMax
</a></h3><div class="s"><div class="hJND5c" style="margin-bottom:2px"><cite>https://www.<b>car</b>max.com/<b>cars</b>
</cite><div class="Pj9hGd"><div style="display:inline" onclick="google.sham(this);" aria-expanded=
"false" aria-haspopup="true" tabindex="0" data-ved="0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQ7B0IWjAP"><span class="CiacGf">
</span></div><div style="display:none" class="am-dropdown-menu" role="menu" tabindex="-1"><ul><li class="mUpfKd">
<a class="imx0m" href="/url?q=http://webcache.googleusercontent.com/search%3Fq%3Dcache:BCMuSnCRjxYJ:https:
//www.carmax.com/cars%252Bcars%26hl%3Den%26gl%3Dus%26ct%3Dclnk&amp;sa=U&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQIAhcMA8&amp;usg=AOvVaw3-rJm1jz8iruVDDfwQMr_1">Cached</a></li><li class="mUpfKd">
<a class="imx0m" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=related:https://www.carmax.com/cars+cars&amp;
tbo=1&amp;sa=X&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQHwhdMA8">Similar</a></li></ul></div>
</div></div>
<span class="st">Search for new and used <b>cars</b> at carmax.com. Use our <b>car</b> search or research <br>
makes and models with customer reviews, expert reviews, and more.</span><br></div></div><div class="g"><h3 class="r">
<a href="/url?q=https://www.cargurus.com/Cars/new/&amp;sa=U&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQFghfMBA&amp;
usg=AOvVaw3_J88TpznNv90S36eoi6gh">New <b>Cars</b> For Sale. Find new <b>cars</b> in your area. - CarGurus</a></h3>
<div class="s"><div class="hJND5c" style="margin-bottom:2px"><cite>https://www.<b>car</b>gurus.com/<b>Cars</b>/new/
</cite><div class="Pj9hGd"><div style="display:inline" onclick="google.sham(this);" aria-expanded="false"
 aria-haspopup="true" tabindex="0" data-ved="0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQ7B0IYDAQ"><span class="CiacGf"></span>
</div><div style="display:none" class="am-dropdown-menu" role="menu" tabindex="-1"><ul><li class="mUpfKd"><a class=
"imx0m" href="/url?q=http://webcache.googleusercontent.com/search%3Fq%3Dcache:_L0frEmznToJ:https://www.cargurus.com
/Cars/new/%252Bcars%26hl%3Den%26gl%3Dus%26ct%3Dclnk&amp;sa=U&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQIAhiMBA&amp;
usg=AOvVaw097wbaaMvQ9kVCAF-S1ZZk">Cached</a></li><li class="mUpfKd"><a class="imx0m" href="/search?hl=en&amp;gl=us&amp;
ie=UTF-8&amp;q=related:https://www.cargurus.com/Cars/new/+cars&amp;tbo=1&amp;sa=X&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQHwhjMBA">Similar</a></li></ul></div></div></div><span class="st">Search new <b>
car</b> listings to find the best local deals. We analyze millions of used <br>
<b>cars</b> daily.</span><br></div></div><div class="g"><h3 class="r">
<a href="/url?q=https://www.autotrader.com/cars-for-sale/&amp;sa=U&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQFghlMBE&amp;usg=AOvVaw2Kcoeaqf9rfKa9gq7hQdc2">Search for <b>Cars
</b> For Sale Online - Find a <b>Car</b> at Autotrader</a></h3><div class="s"><div class="hJND5c" style="margin-bottom:
2px"><cite>https://www.autotrader.com/<b>cars</b>-for-sale/</cite><div class="Pj9hGd"><div style="display:inline
" onclick="google.sham(this);" aria-expanded="false" aria-haspopup="true" tabindex="0" data-ved=
"0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQ7B0IZjAR"><span class="CiacGf"></span></div><div style="display:none" class=
"am-dropdown-menu" role="menu" tabindex="-1"><ul><li class="mUpfKd">
<a class="imx0m" href="/url?q=http://webcache.googleusercontent.com/search%3Fq%3Dcache:qwNd-J6cRhgJ:https:
//www.autotrader.com/cars-for-sale/%252Bcars%26hl%3Den%26gl%3Dus%26ct%3Dclnk&amp;sa=U&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQIAhoMBE&amp;usg=AOvVaw1p67NJvvjGlvy2mtUIiF-I">Cached</a></li></ul>
</div></div></div>
<span class="st">Find new <b>cars</b> and used <b>cars</b> for sale at Autotrader. With millions of <b>cars</b>
, find your <br>
next <b>car</b> at the most complete auto classifieds site online.</span><br></div></div><div class="g"><h3 class="r">
<a href="/url?q=https://www.imdb.com/title/tt0317219/&amp;sa=U&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQFghqMBI&amp;
usg=AOvVaw25_54cSDbvfHqFJkVyQhVG"><b>Cars</b> (2006) - IMDb</a></h3><div class="s"><div class="hJND5c" style=
"margin-bottom:2px"><cite>https://www.imdb.com/title/tt0317219/</cite><div class="Pj9hGd"><div style="display:
inline" onclick="google.sham(this);" aria-expanded="false" aria-haspopup="true" tabindex="0" data-ved=
"0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQ7B0IazAS"><span class="CiacGf"></span></div>
<div style="display:none" class="am-dropdown-menu" role="menu" tabindex="-1"><ul><li class="mUpfKd">
<a class="imx0m" href="/url?q=http://webcache.googleusercontent.com/search%3Fq%3Dcache:OGFS_HZGfGcJ:https://
www.imdb.com/title/tt0317219/%252Bcars%26hl%3Den%26gl%3Dus%26ct%3Dclnk&amp;sa=U&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQIAhtMBI&amp;usg=AOvVaw2m_ZpzbQLwglIwweSPDTud">Cached</a></li></ul></div></div>
</div><div class="f slp"><div class="star"><div style="width:46px">&nbsp;</div></div>&nbsp;Rating: 7.1/10&nbsp;-&nbsp;
318,840 votes</div><span class="st">Directed by John Lasseter, Joe Ranft. With Owen Wilson, Bonnie Hunt, Paul <br>
Newman, Larry the Cable Guy. A hot-shot race-<b>car</b> named Lightning McQueen <br>
gets&nbsp;...</span><br></div></div><div class="g"><h3 class="r">
<a href="/url?q=https://www.carfax.com/Used-Cars-Under-4000_f4&amp;sa=U&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQFghw
MBM&amp;usg=AOvVaw1WtrOudTTWLakF5smy9rXW">Used <b>Cars</b> Under $4,000 for Sale (with Photos) - CARFAX</a></h3>
<div class="s"><div class="hJND5c" style="margin-bottom:2px"><cite>https://www.<b>car</b>fax.com/Used-<b>Cars</b>
-Under-4000_f4</cite><div class="Pj9hGd"><div style="display:inline" onclick="google.sham(this);" aria-expanded=
"false" aria-haspopup="true" tabindex="0" data-ved="0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQ7B0IcTAT"><span class="CiacGf">
</span></div><div style="display:none" class="am-dropdown-menu" role="menu" tabindex="-1"><ul><li class="mUpfKd">
<a class="imx0m" href="/url?q=http://webcache.googleusercontent.com/search%3Fq%3Dcache:c2CfBVnNnvoJ:https://
www.carfax.com/Used-Cars-Under-4000_f4%252Bcars%26hl%3Den%26gl%3Dus%26ct%3Dclnk&amp;sa=U&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQIAhzMBM&amp;usg=AOvVaw1HKGiUJ0r9GGaPSkKecoM7">Cached</a></li></ul></div></div>
</div><span class="st">Every used <b>car</b> for sale comes with a free CARFAX Report. We have 9883 used <br>
<b>cars</b> under $4000 for sale that are reported accident free, 2521 1-Owner <b>cars</b>,&nbsp;...</span><br></div>
</div></ol></div></div></div><div style="clear:both;margin-bottom:17px;overflow:hidden"><div style="font-size:16px;
padding:0 8px 1px">Searches related to <b>cars</b></div><table border="0" cellpadding="0" cellspacing="0"><tr>
<td valign="top"><p class="aw5cc" style="margin:3px 8px"><a href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;
q=cars+for+sale&amp;sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQ1QIIdigA">cars <b>for sale</b></a></p></td>
<td valign="top" style="padding-left:10px"><p class="aw5cc" style="margin:3px 8px"><a href="/search?hl=en&amp;
gl=us&amp;ie=UTF-8&amp;q=cars+for+sale+near+me&amp;sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQ1QIIdygB">cars <b>
for sale near me</b></a></p></td></tr><tr><td valign="top">
<p class="aw5cc" style="margin:3px 8px"><a href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=used+cars&amp;sa=X&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQ1QIIeCgC"><b>used</b> cars</a></p></td><td valign="top" style="padding-left:10px">
<p class="aw5cc" style="margin:3px 8px"><a href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=cars+movie&amp;sa=X&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQ1QIIeSgD">cars <b>movie</b></a></p></td></tr><tr><td valign="top"><p class=
"aw5cc" style="margin:3px 8px"><a href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=used+cars+for+sale&amp;sa=X&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQ1QIIeigE"><b>used</b> cars <b>for sale</b></a></p></td><td valign="top" style=
"padding-left:10px"><p class="aw5cc" style="margin:3px 8px"><a href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;
q=cool+cars&amp;sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQ1QIIeygF"><b>cool</b> cars</a></p></td></tr><tr>
<td valign="top"><p class="aw5cc" style="margin:3px 8px"><a href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=new+cars
&amp;sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQ1QIIfCgG"><b>new</b> cars</a></p></td><td valign="top" style=
"padding-left:10px">
<p class="aw5cc" style="margin:3px 8px"><a href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=car+guru&amp;sa=X&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQ1QIIfSgH">
<b>car guru</b></a></p></td></tr></table></div></div><div id="foot"><table align="center" border="0" cellpadding="0"
cellspacing="0" id="nav"><tr valign="top"><td align="left" class="b"><span class="csb" style="background-position:
-24px 0;width:28px"></span><b></b></td><td><span class="csb" style="background-position:-53px 0;width:20px"></span>
<b>1</b></td><td><a class="fl" href="/search?q=cars&amp;hl=en&amp;gl=us&amp;ie=UTF-8&amp;prmd=ivns&amp;
ei=16NHXKPaGOKU0gKPk6KACw&amp;start=10&amp;sa=N"><span class="csb" style="background-position:-74px 0;width:20px">
</span>2</a></td><td><a class="fl" href="/search?q=cars&amp;hl=en&amp;gl=us&amp;ie=UTF-8&amp;prmd=ivns&amp;
ei=16NHXKPaGOKU0gKPk6KACw&amp;start=20&amp;sa=N"><span class="csb" style="background-position:-74px 0;width:20px">
</span>3</a></td><td><a class="fl" href="/search?q=cars&amp;hl=en&amp;gl=us&amp;ie=UTF-8&amp;prmd=ivns&amp;
ei=16NHXKPaGOKU0gKPk6KACw&amp;start=30&amp;sa=N"><span class="csb" style="background-position:-74px 0;width:20px">
</span>4</a></td><td><a class="fl" href="/search?q=cars&amp;hl=en&amp;gl=us&amp;ie=UTF-8&amp;prmd=ivns&amp;
ei=16NHXKPaGOKU0gKPk6KACw&amp;start=40&amp;sa=N"><span class="csb" style="background-position:-74px 0;width:20px">
</span>5</a></td><td><a class="fl" href="/search?q=cars&amp;hl=en&amp;gl=us&amp;ie=UTF-8&amp;prmd=ivns&amp;
ei=16NHXKPaGOKU0gKPk6KACw&amp;start=50&amp;sa=N"><span class="csb" style="background-position:-74px 0;width:20px">
</span>6</a></td><td><a class="fl" href="/search?q=cars&amp;hl=en&amp;gl=us&amp;ie=UTF-8&amp;prmd=ivns&amp;
ei=16NHXKPaGOKU0gKPk6KACw&amp;start=60&amp;sa=N"><span class="csb" style="background-position:-74px 0;width:20px">
</span>7</a></td>
<td><a class="fl" href="/search?q=cars&amp;hl=en&amp;gl=us&amp;ie=UTF-8&amp;prmd=ivns&amp;
ei=16NHXKPaGOKU0gKPk6KACw&amp;start=70&amp;sa=N"><span class="csb" style="background-position:-74px 0;width:20px">
</span>8</a></td><td><a class="fl" href="/search?q=cars&amp;hl=en&amp;gl=us&amp;ie=UTF-8&amp;prmd=ivns&amp;
ei=16NHXKPaGOKU0gKPk6KACw&amp;start=80&amp;sa=N"><span class="csb" style="background-position:-74px 0;width:20px">
</span>9</a></td><td><a class="fl" href="/search?q=cars&amp;hl=en&amp;gl=us&amp;ie=UTF-8&amp;prmd=ivns&amp;
ei=16NHXKPaGOKU0gKPk6KACw&amp;start=90&amp;sa=N"><span class="csb" style="background-position:-74px 0;width:20px">
</span>10</a></td><td class="b" style="text-align:left">
<a class="fl" href="/search?q=cars&amp;hl=en&amp;gl=us&amp;ie=UTF-8&amp;prmd=ivns&amp;ei=16NHXKPaGOKU0gKPk6KACw&amp;
start=10&amp;sa=N" style="text-align:left"><span class="csb" style="background-position:-96px 0;width:71px"></span>
<span style="display:block;margin-left:53px">Next</span></a></td></tr></table><p class="A8ul6" id="bfl" style="margin:
19px 0 0;text-align:center"><a href="/advanced_search?q=cars&amp;hl=en&amp;gl=us&amp;ie=UTF-8&amp;prmd=ivns">
Advanced search</a><a href="/support/websearch/bin/answer.py?answer=134479&amp;hl=en">Search Help</a> <a href=
"/tools/feedback/survey/html?productId=196&amp;query=cars&amp;hl=en">Send feedback</a></p><div class="A8ul6" id="fll"
style="margin:19px auto 19px auto;text-align:center">
<a href="/">Google&nbsp;Home</a> <a href="/intl/en/ads">Advertising&nbsp;Programs</a>
<a href="/services">Business Solutions</a> <a href="/intl/en/policies/privacy/">Privacy</a>
<a href="/intl/en/policies/terms/">Terms</a> <a href="/intl/en/about.html">About Google</a></div></div></td>
<td id="rhs_block" valign="top"><ol><div class="g"><div class="VBt9Dc hp-xpdbox"><div class="R8KuR" style="float:right">
<div class="OSMzvb" style="height:160px;width:86px">
<a href="/url?q=https://www.wired.com/story/future-cars-roundup-sep-15/&amp;sa=U&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQndQBCIcBMBQ&amp;usg=AOvVaw03h1u-r0S3M4yCPuCj392Q">
<img src="https://encrypted-tbn0.gstatic.com/images?
q=tbn:ANd9GcTb9YmEzdGCgw1DyQdx8rDOAIKmxaKWZ9VdOidb6BsbtscDoMLj3BRirgsw" style="margin-left:-59px;margin-right
:-68px" title="https://www.wired.com/story/future-cars-roundup-sep-15/" alt="Image result for cars"></a></div></div>
<div class="V7Q8V"><div><div class="FSP1Dd">Car</div><div class="F7uZG Rlw09">Transportation mode</div></div></div>
<div class="V7Q8V"><div class="mraOPb">
<span>A car is a wheeled motor vehicle used for transportation. Most definitions of car say they run primarily on roads,
seat one to eight people, have four tires, and mainly transport people rather than goods. Cars came into global use
during the 20th century, and developed economies depend on them. <a class="fl" href="/url?q=https://en.wikipedia.org/
wiki/Car&amp;sa=U&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQmhMIjQEoADAW&amp;usg=AOvVaw0K0WB_-8gTUCdknhQaX03r">
Wikipedia</a></span></div></div><div class="V7Q8V" style="display:none"></div><div class="V7Q8V"><span class="cC4Myd">
Inventor: </span><span class="A1t5ne"><a class="A1t5ne fl" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=Karl+Benz
&amp;stick=H4sIAAAAAAAAAOPgE2LXz9U3yDbJUuIAMUwsK9K1dDPKrfST83NyUpNLMvPzkJjxyYklqen5RZmpxVaZeWWpeSX5RQCwgDGtRAAAAA&amp;
sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQmxMIkQEoADAY">Karl Benz</a></span></div><div class="dXAUyb">
<div class="lHETUb">Types of Cars</div><div class="xKoZHf B27ELd" style="width:72px">
<div class="tQOFN" style="height:72px">
<a class="FEM55" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=Mid-size+car&amp;
stick=H4sIAAAAAAAAAONgFmLXz9U3yDbJUuIEMYzL8kpMtESyk630k_Nzc_PzrFLyy_PKE4tSilcxygHFcnJSk0sy8_P0E0tL8nPzSzLLUuOTc
xKLi1OLARYWseVNAAAA&amp;sa=X&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQsQ4IlQEwGQ">
<img alt="Mid-size car" height="72px" src="https://encrypted-tbn2.gstatic.com/images?
q=tbn:ANd9GcQO9g3MOndtH6iKFlahWC2WXsWMLIBTj7RVImrkff-TKC3YNa99wkZn0j9Tj9eltTRKdiI" title="Mid-size car" width="72px">
</a></div><div class="brYqc">
<a class="fl" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=Mid-size+car&amp;
stick=H4sIAAAAAAAAAONgFmLXz9U3yDbJUuIEMYzL8kpMtESyk630k_Nzc_PzrFLyy_PKE4tSilcxygHFcnJSk0sy8_P0E0tL8nPzSzLLUuOTcx
KLi1OLARYWseVNAAAA&amp;sa=X&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQxA0IlgEwGQ" title="
Mid-size car">Mid&#8209;size car</a><div class="czonVc" title="Mid-size car"></div></div></div>
<div class="B27ELd" style="width:72px"><div class="tQOFN" style="height:72px">
<a class="FEM55" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=Sedan&amp;
stick=H4sIAAAAAAAAAONgFmLXz9U3yDbJUuIEMYwMcwuMtESyk630k_Nzc_PzrFLyy_PKE4tSilcxygHFcnJSk0sy8_P0E0tL8nPzS
zLLUuOTcxKLi1OLAYy3vpNNAAAA&amp;sa=X&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQsQ4ImAEwGQ">
<img alt="Sedan" height="72px" src="https://encrypted-tbn1.gstatic.com/images?
q=tbn:ANd9GcRnyoVHKf5a242jpmt5L5g3PWp3LEAxz_ZcKQFQWlpcN5U_me27hiTUBv3yKoXWP_xBasc" title="Sedan" width="72px">
</a></div>
<div class="brYqc"><a class="fl" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=Sedan&amp;
stick=H4sIAAAAAAAAAONgFmLXz9U3yDbJUuIEMYwMcwuMtESyk630k_Nzc_PzrFLyy_PKE4tSilcxygHFcnJSk0sy8_P0E0tL8nPzS
zLLUuOTcxKLi1OLAYy3vpNNAAAA&amp;sa=X&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQxA0ImQEwGQ" title="Sedan">Sedan</a>
<div class="czonVc" title="Sedan"></div></div></div>
<div class="ty7XEe B27ELd" style="width:72px">
<div class="tQOFN" style="height:72px">
<a class="FEM55" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=Sport+utility+vehicle&amp;
stick=H4sIAAAAAAAAAONgFmLXz9U3yDbJUuIAMZJLigq0RLKTrfST83Nz8_OsUvLL88oTi1KKVzHKAcVyclKTSzLz8_QTS0vyc_NLMst
S45NzEouLU4sB_9ykeUwAAAA&amp;sa=X&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQsQ4ImwEwGQ">
<img alt="Sport utility vehicle" height="72px" src="https://encrypted-tbn2.gstatic.com/images?
q=tbn:ANd9GcTw2agno4HHjl5Bg7yCj8z4EbIPaBw6phobzqL1c5PJ-hZ8i0j-SWzIc6W09rK9s8Jr2_Q" title=
"Sport utility vehicle" width="72px"></a></div>
<div class="brYqc"><a class="fl" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=Sport+utility+vehicle&amp;
stick=H4sIAAAAAAAAAONgFmLXz9U3yDbJUuIAMZJLigq0RLKTrfST83Nz8_OsUvLL88oTi1KKVzHKAcVyclKTSzLz8_QTS0vyc_NLMst
S45NzEouLU4sB_9ykeUwAAAA&amp;
sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQxA0InAEwGQ" title="Sport utility vehicle">Sport utility vehicle</a>
<div class="czonVc" title="Sport utility vehicle"></div></div></div><br>
<div class="xKoZHf B27ELd" style="width:72px"><div class="tQOFN" style="height:72px">
<a class="FEM55" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=Compact+car&amp;
stick=H4sIAAAAAAAAAONgFmLXz9U3yDbJUuIEMYyKy6vitUSyk630k_Nzc_PzrFLyy_PKE4tSilcxygHFcnJSk0sy8_P0E0tL8nPz
SzLLUuOTcxKLi1OLAYxXKm5NAAAA&amp;sa=X&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQsQ4IngEwGQ">
<img alt="Compact car" height="72px" src="https://encrypted-tbn1.gstatic.com/images?
q=tbn:ANd9GcTjnNGPIKNLClpL19F16kMDBZG_1HldQaB3mXu7ZDoizVRdfIlZ6N5scJbsEVGEIMiRw80" title="Compact car" width="72px">
</a></div>
<div class="brYqc"><a class="fl" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=Compact+car&amp;
stick=H4sIAAAAAAAAAONgFmLXz9U3yDbJUuIEMYyKy6vitUSyk630k_Nzc_PzrFLyy_PKE4tSilcxygHFcnJSk0sy8_P0E0tL8nP
zSzLLUuOTcxKLi1OLAYxXKm5NAAAA&amp;sa=X&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQxA0InwEwGQ" title="Compact car">Compact car</a>
<div class="czonVc" title="Compact car"></div></div></div>
<div class="B27ELd" style="width:72px"><div class="tQOFN" style="height:72px">
<a class="FEM55" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=City+car&amp;
stick=H4sIAAAAAAAAAONgFmLXz9U3yDbJUuIEMYzNLIuLtUSyk630k_Nzc_PzrFLyy_PKE4tSilcxygHFcnJSk0sy8_P0E0t
L8nPzSzLLUuOTcxKLi1OLAQjPAyFNAAAA&amp;sa=X&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQsQ4IoQEwGQ">
<img alt="City car" height="72px" src="https://encrypted-tbn2.gstatic.com/images?
q=tbn:ANd9GcRstSpHeMTDOVfWRJF1KZTYG-WVdoKkZaq-kV-tI89AORbFOaUdfsTBkqDnwlF0lPeD0dU" title="City car" width="72px">
</a></div>
<div class="brYqc"><a class="fl" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=City+car&amp;
stick=H4sIAAAAAAAAAONgFmLXz9U3yDbJUuIEMYzNLIuLtUSyk630k_Nzc_PzrFLyy_PKE4tSilcxygHFcnJSk0sy8_P0E0tL8nPzSz
LLUuOTcxKLi1OLAQjPAyFNAAAA&amp;sa=X&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQxA0IogEwGQ" title="City car">City car</a>
<div class="czonVc" title="City car"></div></div></div>
<div class="ty7XEe B27ELd" style="width:72px"><div class="tQOFN" style="height:72px">
<a class="FEM55" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=Convertible&amp;
stick=H4sIAAAAAAAAAONgFmLXz9U3yDbJUuIEMQwtC8sttUSyk630k_Nzc_PzrFLyy_PKE4tSilcxygHFcnJSk0sy8_P0E0tL8nPzS
zLLUuOTcxKLi1OLAUs26tZNAAAA&amp;sa=X&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQsQ4IpAEwGQ">
<img alt="Convertible" height="72px" src="https://encrypted-tbn2.gstatic.com/images?
q=tbn:ANd9GcTjbmT5-F81WhpmLkJ6SQH0fheS7YDV445ysyJPmHHyK6AYZFWjMOVSlhu5PA39j5l0tKo" title="Convertible" width="72px">
</a></div>
<div class="brYqc"><a class="fl" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=Convertible&amp;
stick=H4sIAAAAAAAAAONgFmLXz9U3yDbJUuIEMQwtC8sttUSyk630k_Nzc_PzrFLyy_PKE4tSilcxygHFcnJSk0sy
8_P0E0tL8nPzSzLLUuOTcxKLi1OLAUs26tZNAAAA&amp;
sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQxA0IpQEwGQ" title="Convertible">Convertible</a>
<div class="czonVc" title="Convertible"></div></div></div><br></div><div class="dXAUyb">
<div class="lHETUb">People also search for</div><div class="xKoZHf B27ELd" style="width:72px">
<div class="tQOFN" style="height:72px"><a class="FEM55" href="/search?hl=en&amp;
gl=us&amp;ie=UTF-8&amp;
q=Tire&amp;stick=H4sIAAAAAAAAAONgFmLXz9U3yDbJUuIAMTIsc8u0-Jzzc3Pz84IzU1LLEyuLAVROpLUlAAAA&amp;sa=X&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQsQ4IqQEwGg">
<img alt="Motor Vehicle Tires" height="72px" src="https://encrypted-tbn0.gstatic.com/images?
q=tbn:ANd9GcRNjuiXE7xlAZiYDXDsyyR1j0-aOAEQ9F0e2Uv5KhU1wHOZkdGbLjk" title="Motor Vehicle Tires" width="72px">
</a></div>
<div class="brYqc"><a class="fl" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=Tire&amp;
stick=H4sIAAAAAAAAAONgFmLXz9U3yDbJUuIAMTIsc8u0-Jzzc3Pz84IzU1LLEyuLAVROpLUlAAAA&amp;sa=X&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQxA0IqgEwGg" title="Motor Vehicle Tires">Motor Vehicle Tires</a>
<div class="czonVc" title="Motor Vehicle Tires"></div></div></div>
<div class="B27ELd" style="width:72px"><div class="tQOFN" style="height:72px">
<a class="FEM55" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=Bicycle&amp;
stick=H4sIAAAAAAAAAONgFmLXz9U3yDbJUuIAMQwtLdO1-Jzzc3Pz84IzU1LLEyuLAdMBV5clAAAA&amp;sa=X&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQsQ4IrAEwGg">
<img alt="Bicycles" height="72px" src="https://encrypted-tbn0.gstatic.com/images?
q=tbn:ANd9GcQuE2xASHdZfnPJrR1xx5ip8jimRyGSpti1BwpKLvWdGtonuLPGs3ewYRo4aqD13KX-aK4" title=
"Bicycles" width="72px"></a></div>
<div class="brYqc"><a class="fl" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;
q=Bicycle&amp;
stick=H4sIAAAAAAAAAONgFmLXz9U3yDbJUuIAMQwtLdO1-Jzzc3Pz84IzU1LLEyuLAdMBV5clAAAA&amp;sa=X&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQxA0IrQEwGg" title="Bicycles">Bicycles</a>
<div class="czonVc" title="Bicycles"></div></div></div>
<div class="ty7XEe B27ELd" style="width:72px"><div class="tQOFN" style="height:72px">
<a class="FEM55" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=Airplane&amp;
stick=H4sIAAAAAAAAAONgFmLXz9U3yDbJUuICMUyTq6rMcrT4nPNzc_PzgjNTUssTK4sBFQM3oicAAAA&amp;sa=X&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQsQ4IrwEwGg">
<img alt="Airplane" height="72px" src="https://encrypted-tbn3.gstatic.com/images?
q=tbn:ANd9GcQ-lKUilotozZ05K4WNBmh2FBbD0DvZg0WZH46_I64pRIwM-DC_Fni-SKkMQe9NZ7cXPYI" title="Airplane" width="72px">
</a></div>
<div class="brYqc"><a class="fl" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=Airplane&amp;
stick=H4sIAAAAAAAAAONgFmLXz9U3yDbJUuICMUyTq6rMcrT4nPNzc_PzgjNTUssTK4sBFQM3oicAAAA&amp;sa=X&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQxA0IsAEwGg" title="Airplane">Airplane</a>
<div class="czonVc" title="Airplane"></div></div></div><br>
<div class="xKoZHf B27ELd" style="width:72px"><div class="tQOFN" style="height:72px">
<a class="FEM55" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=Mobile+phone&amp;
stick=H4sIAAAAAAAAAONgFmLXz9U3yDbJUuIAMUwNsi20-Jzzc3Pz84IzU1LLEyuLAfD_lholAAAA&amp;sa=X&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQsQ4IsgEwGg">
<img alt="Mobile Phones" height="72px" src="https://encrypted-tbn1.gstatic.com/images?q=tbn:
ANd9GcR_gKEa8STJQ8HjHehp3P2zgqb6j3eYQ94NB7flTZyiQEOqNqmbetr9oReD7GuslZD1kJY" title="Mobile Phones" width="72px">
</a></div>
<div class="brYqc"><a class="fl" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=Mobile+phone&amp;
stick=H4sIAAAAAAAAAONgFmLXz9U3yDbJUuIAMUwNsi20-Jzzc3Pz84IzU1LLEyuLAfD_lholAAAA&amp;sa=X&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQxA0IswEwGg" title="Mobile Phones">Mobile Phones</a>
<div class="czonVc" title="Mobile Phones"></div></div></div>
<div class="B27ELd" style="width:72px"><div class="tQOFN" style="height:72px">
<a class="FEM55" href="/search?hl=en&amp;
gl=us&amp;ie=UTF-8&amp;q=Photograph&amp;
stick=H4sIAAAAAAAAAONgFmLXz9U3yDbJUuIAMcwsslK0-Jzzc3Pz84IzU1LLEyuLAYaNw4wlAAAA&amp;sa=X&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQsQ4ItQEwGg"><img alt="Photograph" height="72px" src=
"https://encrypted-tbn0.gstatic.com/images?
q=tbn:ANd9GcQwUHtLufHyHTVJ2PRue0XkzavaSrBooQgUZETuIsjkAyLLYqiGd84hq8BSht5W8YLj5zk" title=
"Photograph" width="72px"></a></div>
<div class="brYqc"><a class="fl" href="/search?hl=en&amp;gl=us&amp;
ie=UTF-8&amp;q=Photograph&amp;stick=H4sIAAAAAAAAAONgFmLXz9U3yDbJUuIAMcwsslK0-Jzzc3Pz84IzU1LLEyuLAYaNw4wlAAAA&amp;
sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQxA0ItgEwGg" title="Photograph">Photogra...</a><
div class="czonVc" title="Photograph"></div></div></div><div class="ty7XEe B27ELd" style="width:72px">
<div class="tQOFN" style="height:72px">
<a class="FEM55" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;
q=Map&amp;stick=H4sIAAAAAAAAAONgFmLXz9U3yDbJUuIAMUziS5K0-Jzzc3Pz84IzU1LLEyuLAeQTBfclAAAA&amp;
sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQsQ4IuAEwGg">
<img alt="Map" height="72px" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:
ANd9GcSAniSQ0z08lHoBfXAFiELFoUILK2s0Xt98s-ktLfyL7H2rFhCdb4xO0kReoTEN-haiibg" title="Map" width="72px">
</a></div>
<div class="brYqc"><a class="fl" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=Map&amp;
stick=H4sIAAAAAAAAAONgFmLXz9U3yDbJUuIAMUziS5K0-Jzzc3Pz84IzU1LLEyuLAeQTBfclAAAA&amp;sa=X&amp;
ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQxA0IuQEwGg" title="Map">Map</a>
<div class="czonVc" title="Map"></div></div></div><br></div></div></div><div class="g"><div id="k2fPW">
<div class="u6RhQc"><div><div class="CB9G1b">See results about</div>
</div></div><div class="u6RhQc"><div class="TyXs8d"><table class="NWncrd">
<tr><td class="rNjNwd"><a class="fl" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=Cars+3&amp;
stick=H4sIAAAAAAAAAONgecQYzC3w8sc9YSmvSWtOXmN04eIKzsgvd80rySypFNLiYoOyFLj4pbj1c_UNDA3Sq4zTDDQYpHi5kAWUuJr2rTjExsLBKMDAAwBCptzSWAAAAA&amp;sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQ-DIIwQEwHA">
<div class="JYQZge vrQIef">Cars 3 (2017 film)</div><div class="C6ZAab">Blindsided by a new generation of blazing&#8209;
fast cars, the legendary ...</div></a></td>
<td width="40"><a href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;
q=Cars+3&amp;stick=H4sIAAAAAAAAAONgecQYzC3w8sc9YSmvSWtOXmN04eIKzsgvd80rySypFNLiYoOyFLj4pbj1c_UNDA3Sq4zTDDQYpHi5kAWUuJr2rTjExsLBKMDAAwBCptzSWAAAAA&amp;sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQ-DIIwgEwHA">
<img class="DBHfJe"
 src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRyVKr4u4AY0Ab_53VcX6mvZIT2ExKepht9g30La1hUsJkQZm57VvfUjA"
height="40" width="40"></a></td></tr></table></div></div>
<div class="u6RhQc"><div class="TyXs8d"><table class="NWncrd"><tr><td class="rNjNwd">
<a class="fl" href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=Cars+(franchise)&amp;
stick=H4sIAAAAAAAAAONgecQYyC3w8sc9YSmPSWtOXmN04uIKzsgvd80rySypFNLgYoOy5Lj4pLj0c_UN0isNk4uLNRikeLiQ-EpcTftWHGJj4WAUYOABAAMQnBxWAAAA&amp;sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQ-DIIxQEwHQ">
<div class="JYQZge vrQIef">Cars (Film series)</div><div class="C6ZAab">
Cars is a CGI&#8209;animated film series and Disney media franchise set in a world ...</div></a></td>
<td width="40"><a href="/search?hl=en&amp;gl=us&amp;ie=UTF-8&amp;q=Cars+(franchise)&amp;
stick=H4sIAAAAAAAAAONgecQYyC3w8sc9YSmPSWtOXmN04uIKzsgvd80rySypFNLgYoOy5Lj4pLj0c_UN0isNk4uLNRikeLiQ-EpcTftWHGJj4WAUYOABAAMQnBxWAAAA&amp;sa=X&amp;ved=0ahUKEwjjoZaewoLgAhViilQKHY-JCLAQ-DIIxgEwHQ">
<img class="DBHfJe" src="https://encrypted-tbn0.gstatic.com/images?
q=tbn:ANd9GcSvni_uP6i5jyTl195E4Omy4QKmZbNe8Iq-K30tfZmRCslrOi8VlPpGvg" height="40" width="40">
</a></td></tr></table></div></div></div></div>
<div class="g"></div></ol></td></tr></tbody></table><script type="text/javascript"
 nonce="cIrvPG0MvCAr3nWe2roe/g==">(function(){var eventid='16NHXKPaGOKU0gKPk6KACw';google.kEI = eventid;})();</script>
<script src="/xjs/_/js/k=xjs.hp.en_US.nHwsRkntBGI.O/m=sb_he,d/rt=j/d=1/rs=ACT90oHERx1Tyfg9pczIvhJ-CJ3zvX5C4Q"
nonce="cIrvPG0MvCAr3nWe2roe/g=="></script>
<script type="text/javascript"
nonce="cIrvPG0MvCAr3nWe2roe/g==">google.ac&&google.ac.c({"agen":true,"cgen":true,"client":"heirloom-serp"
,"dh":true,"dhqt":true,"ds":"","ffql":"en","fl":true,"host":"google.com","isbh":28,"jsonp":true,"msgs":{"cibl":"Clear
Search","dym":"Did you mean:","lcky":"Imim Feeling Lucky",
"lml":"Learn more","oskt":"Input tools","psrc":"This search was removed from your Web History",
"psrl":"Remove","sbit":"Search by image","srch":"Google Search"},"ovr":{},"pq":"cars","refpd":true,
"rfs":["cars for sale","used cars","used cars for sale","new cars",
"cars for sale near me","cars movie","cool cars","car guru"],
"sbpl":24,"sbpr":24,"scd":10,"sce":5,"stok":"bUuAGFPHsa21Kcx6aTf3ScwvnRs","uhde":false})</script>
<script nonce="cIrvPG0MvCAr3nWe2roe/g==">(function(){window.google.cdo={height:0,width:0};
(function(){var a=window.innerWidth,b=window.innerHeight;if(!a||!b)
{var c=window.document,d="CSS1Compat"==c.compatMode?c.documentElement:c.body;
a=d.clientWidth;b=d.clientHeight}a&&b&&(a!=google.cdo.width||b!=google.cdo.height)&&
google.log("","","/client_204?&atyp=i&biw="+a+"&bih="+b+"&ei="+google.kEI);}).call(this);})();</script>
</body></html> """

# '<html><head><title>Cars</title></head><body><h1>Search Results: Cars</h1></body></html>'

mockDataKittens = {
    "search_metadata": {},
    "search_parameters": {"q": "kittens"},
    "search_information": {"total_results": "About 512,000,000 results"},
    "ads": [],
    "local_map": {},
    "local_results": [],
    "related_questions": [],
    "answer_box": {},
    "organic_results": [
        {
            "position": 0,
            "title": "How To Look After A Kitten | Purina",
            "link": "https://www.purina.com.au/kittens&"
            "sa=U&ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0QFgg3MAM&usg=AOvVaw1T4GNmMT3b2oQoB2Hn4SwQ",
            "snippet": "Purina Has Lots Of Vet Advice On Kitten Care, Including How To "
            "Feed And Train Your New Kitten, Designed To Help You And Your Kitten Live Happily Together.",
        },
        {
            "position": 1,
            "title": "Kittens Do Things For The First Time - YouTube",
            "link": "https://www.youtube.com/watch%3Fv%3Dc1c0a4fo1zo&"
            "sa=U&ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0QtwIIPTAE&usg=AOvVaw3_KNNoD4nPj1-jIO5G0apd",
            "snippet": "Feb 26, 2015 - 1 min - Uploaded by BuzzFeedVideoCan you handle this "
            "level of cute? Check out Buzzfeed's new Cute Or Not app!  http://bit.ly ...",
        },
        {
            "position": 2,
            "title": "Kittens see / do things for the first time - Funny and cute cat ...",
            "link": "https://www.youtube.com/watch%3Fv%3DmmjlMgDSYFo&"
            "sa=U&ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0QtwIIQTAF&usg=AOvVaw3EQJOn9wSe-w9D3rUpwvUH",
            "snippet": "Apr 27, 2016 - 6 min - Uploaded by Tiger ProductionsPuppies see / "
            "do things for the first time - Funny and cute dog compilation : https:// www.youtube ...",
        },
        {
            "position": 3,
            "title": "News for kittens",
            "link": "?q=kittens&hl=en&gl=us&ie=UTF-8&prmd=ivns&source=univ&"
            "tbm=nws&tbo=u&sa=X&ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0QqAIIRA",
            "snippet": "What's being called the first-in-America kitten-only place to rest, "
            "relax and interact with kittens between the ages of three-to-six months will open...",
        },
        {
            "position": 4,
            "title": "Why Adopt - Kitten Rescue",
            "link": "https://kittenrescue.org/adopt/&sa=U&"
            "ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0QFghNMAk&usg=AOvVaw0DQe-Py_NZ3-bZDtcKQ2XC",
            "snippet": "Our work is most rewarding when we're able to adopt a cat or a kitten "
            "into a loving home. Adopting gives an animal a second chance at life.",
        },
        {
            "position": 5,
            "title": "Kitten - Wikipedia",
            "link": "https://en.wikipedia.org/wiki/Kitten&sa=U&"
            "ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0QFghSMAo&usg=AOvVaw2D3pkMVRf1VyjdTccJZ-Ju",
            "snippet": "A kitten is a juvenile cat. After being born, kittens are totally "
            "dependent on their mother for survival and they do not normally open their eyes until after seven to...",
        },
        {
            "position": 6,
            "title": "Images for kittens",
            "link": "?q=kittens&hl=en&gl=us&ie=UTF-8&prmd=ivns&tbm=isch&tbo=u&source=univ&sa=X&"
            "ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0QsAQIWA",
            "snippet": "Kitten care and training information. ... Your new kitten deserves "
            "the best possible start in life. ... Nutrition Tips for Kittens Kittens have special nutritional needs.",
        },
        {
            "position": 7,
            "title": "Healthy Cats Guide: Caring for Your Kitten - Healthy Pets - WebMD",
            "link": "https://pets.webmd.com/cats/guide/kitten-care&sa=U&"
            "ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0QFghkMBA&usg=AOvVaw2mP1n4nI57_Db_URP1dian",
            "snippet": "(If you've been raising the kittens for a few weeks already, "
            "congratulations-the hardest part is over!) Kittens at this age will start "
            "weaning (meaning they'll slowly...",
        },
        {
            "position": 8,
            "title": "Alley Cat Allies | How Old Is That Kitten? Kitten Guide: Four Weeks",
            "link": "https://www.alleycat.org/resources/how-old-is-that-kitten-guide-four-weeks/&"
            "sa=U&ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0QFghpMBE&usg=AOvVaw1mZtemKX3mMpC0nQQqOvgm",
            "snippet": "At about seven days old, kittens' ears will unfold and their "
            "eyes may start to open, though their eyesight is still unfocused. They have "
            "doubled their birth weight to...",
        },
        {
            "position": 9,
            "title": "Alley Cat Allies | How Old Is That Kitten? Kitten Guide: One Week",
            "link": "https://www.alleycat.org/resources/how-old-is-that-kitten-guide-one-week/&sa=U&"
            "ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0QFghvMBI&usg=AOvVaw3qcxs_ZK2A03oNeq0EsqrP",
            "snippet": "",
        },
    ],
    "related_searches": [
        {
            "query": "kittens video",
            "link": "/search?hl=en&gl=us&ie=UTF-8&q=kittens+video&sa=X&"
            "ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0Q1QIIdSgA",
        },
        {
            "query": "kittens near me",
            "link": "/search?hl=en&gl=us&ie=UTF-8&q=kittens+near+me&sa=X&"
            "ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0Q1QIIdigB",
        },
        {
            "query": "kittens for sale",
            "link": "/search?hl=en&gl=us&ie=UTF-8&q=kittens+for+sale&sa=X&"
            "ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0Q1QIIdygC",
        },
        {
            "query": "kittens 2017",
            "link": "/search?hl=en&gl=us&ie=UTF-8&q=kittens+2017&sa=X&"
            "ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0Q1QIIeCgD",
        },
        {
            "query": "baby kittens",
            "link": "/search?hl=en&gl=us&ie=UTF-8&q=baby+kittens&sa=X&"
            "ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0Q1QIIeSgE",
        },
        {
            "query": "free kittens",
            "link": "/search?hl=en&gl=us&ie=UTF-8&q=free+kittens&sa=X&"
            "ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0Q1QIIeigF",
        },
        {
            "query": "kittens for adoption",
            "link": "/search?hl=en&gl=us&ie=UTF-8&q=kittens+for+adoption&sa=X&"
            "ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0Q1QIIeygG",
        },
        {
            "query": "lots of kittens",
            "link": "/search?hl=en&gl=us&ie=UTF-8&q=lots+of+kittens&sa=X&"
            "ved=0ahUKEwjhh8_Qr_jfAhXnLLkGHQGKAE0Q1QIIfCgH",
        },
    ],
    "pagination": {},
}

mockDataCats = {
    "search_metadata": {},
    "search_parameters": {"q": "cats"},
    "search_information": {"total_results": "About 5,030,000,000 results"},
    "ads": [],
    "local_map": {},
    "local_results": [],
    "related_questions": [],
    "answer_box": {},
    "organic_results": [
        {
            "position": 0,
            "title": "Cats the Musical - Official Website & Tickets",
            "link": "https://www.catsthemusical.com/&sa=U&"
            "ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQFggUMAA&usg=AOvVaw1tGzR0ChHcOE6VAFRtFUXl",
            "snippet": "The official home of Andrew Lloyd Webber's world-famous, family-favourite "
            "musical CATS - Tickets from $20 & NO booking fee!",
        },
        {
            "position": 1,
            "title": "Complete Guide to Caring for Cats | Cat Breed Information, Cat ...",
            "link": "http://www.vetstreet.com/cats/&sa=U&"
            "ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQFggZMAE&usg=AOvVaw3afMRFiGgWwZhhhwBzYnbi",
            "snippet": "Your cat's online owners manual, featuring articles about breed "
            "information, cat selection, training, grooming and care for cats and kittens.",
        },
        {
            "position": 2,
            "title": "Cat Breed Collection | Purina",
            "link": "https://www.purina.com/cats/cat-breeds&sa=U&"
            "ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQFggfMAI&usg=AOvVaw3Tg6RZQt3rYkusIsA-y-Bg",
            "snippet": "Trying to decide what type of cat is right for you and your family? "
            "Browse through our list of popular cat breeds, and find the best breed for your lifestyle.",
        },
        {
            "position": 3,
            "title": "News for cats",
            "link": "?q=cats&hl=en&gl=us&ie=UTF-8&prmd=ivnsb&source=univ&"
            "tbm=nws&tbo=u&sa=X&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQqAIIJQ",
            "snippet": "A stray kitten appropriately named Loco started Mr. Chandoha on "
            "an unexpected career. By the time he died, he had taken some 90000 cat...",
        },
        {
            "position": 4,
            "title": "Cats | Animal Planet",
            "link": "http://www.animalplanet.com/pets/cats/&sa=U&"
            "ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQFgguMAY&usg=AOvVaw2U4ogL8tY1DG92EDQPkzQz",
            "snippet": "Explore our guide to cats, kittens and their habitats. Learn "
            "about over a hundred different cat breeds and how to deal with troubled cats.",
        },
        {
            "position": 5,
            "title": "Cats: Adoption, Bringing A Cat Home and Care - Petfinder",
            "link": "https://www.petfinder.com/cats/&sa=U&"
            "ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQFgg0MAc&usg=AOvVaw0R_Hk5SBzL0yjJCg72g77j",
            "snippet": "Everything you need to know about how to adopt a cat, bringing "
            "your new cat home, cat health and care and more!",
        },
        {
            "position": 6,
            "title": "Cats (musical) - Wikipedia",
            "link": "https://en.wikipedia.org/wiki/Cats_(musical)&sa=U&"
            "ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQFgg6MAg&usg=AOvVaw17khzwFW-gMi-s8RxuZRf_",
            "snippet": "Cats is a sung-through musical composed by Andrew Lloyd Webber, "
            "based on Old Possum's Book of Practical Cats by T. S. Eliot. The musical tells the story of a...",
        },
        {
            "position": 7,
            "title": "Cat - Wikipedia",
            "link": "https://en.wikipedia.org/wiki/Cat&sa=U&"
            "ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQFghAMAk&usg=AOvVaw0QkzMUSua1IVxNeypH-8K4",
            "snippet": "The cat often referred to as the domestic cat to distinguish it"
            " from its wild relatives such as tigers, lions, and other "
            "felids and felines, is a small furry, carnivorous...",
        },
        {
            "position": 8,
            "title": "Cat Health Center | Cat Care and Information from WebMD",
            "link": "https://www.webmd.com/pets/cats/default.htm&"
            "sa=U&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQFghGMAo&usg=AOvVaw19GXi0bR2FY7GvWIz4wGvy",
            "snippet": "WebMD veterinary experts provide comprehensive information about"
            " cat health care, offer nutrition and feeding tips, and help you identify illnesses in cats.",
        },
        {
            "position": 9,
            "title": "Images for cats",
            "link": "?q=cats&hl=en&gl=us&ie=UTF-8&prmd=ivnsb&tbm=isch&"
            "tbo=u&source=univ&sa=X&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQsAQISw",
            "snippet": "",
        },
    ],
    "related_searches": [
        {
            "query": "cats breeds",
            "link": "/search?hl=en&gl=us&ie=UTF-8&q=cats+breeds&"
            "sa=X&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQ1QIIWCgA",
        },
        {
            "query": "cute cats",
            "link": "/search?hl=en&gl=us&ie=UTF-8&q=cute+cats&"
            "sa=X&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQ1QIIWSgB",
        },
        {
            "query": "cats musical",
            "link": "/search?hl=en&gl=us&ie=UTF-8&q=cats+musical&"
            "sa=X&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQ1QIIWigC",
        },
        {
            "query": "facts about cats",
            "link": "/search?hl=en&gl=us&ie=UTF-8&q=facts+about+cats&"
            "sa=X&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQ1QIIWygD",
        },
        {
            "query": "cats broadway",
            "link": "/search?hl=en&gl=us&ie=UTF-8&q=cats+broadway&"
            "sa=X&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQ1QIIXCgE",
        },
        {
            "query": "c.a.t.s game",
            "link": "/search?hl=en&gl=us&ie=UTF-8&q=c.a.t.s+game&"
            "sa=X&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQ1QIIXSgF",
        },
        {
            "query": "cats for sale",
            "link": "/search?hl=en&gl=us&ie=UTF-8&q=cats+for+sale&"
            "sa=X&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQ1QIIXigG",
        },
        {
            "query": "cats movie",
            "link": "/search?hl=en&gl=us&ie=UTF-8&q=cats+movie&"
            "sa=X&ved=0ahUKEwjcwuqcvPjfAhUEh-AKHYD_AxYQ1QIIXygH",
        },
    ],
    "pagination": {},
}

mockDataCars = {
    "search_metadata": {},
    "search_parameters": {"q": "cars"},
    "search_information": {"total_results": "About 11,000,000,000 results"},
    "ads": [],
    "local_map": {},
    "local_results": [],
    "related_questions": [],
    "answer_box": {},
    "organic_results": [
        {
            "position": 0,
            "title": "New Cars, Used Cars, Car Reviews and News | Cars.com",
            "link": "https://www.cars.com/&sa=U&ved="
            "0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQFggVMAA&usg=AOvVaw0pprhkLhExhjGt1J3H5Cuu",
            "snippet": "Research and compare cars, find local dealers/sellers, calculate"
            " loan payments, find your car's value, sell or trade your car, get a service estimate, and much...",
        },
        {
            "position": 1,
            "title": "Cars for Sale",
            "link": "https://www.cars.com/shopping/&sa=U&ved="
            "0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQjBAIHDAB&usg=AOvVaw2D3fPz3Vb3v2Of8c8f_9LY",
            "snippet": "Browse cars for sale on Cars.com. Shop the best deals near you ...",
        },
        {
            "position": 2,
            "title": "Sell Your Car",
            "link": "https://www.cars.com/sell/&sa=U&ved="
            "0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQjBAIHjAE&usg=AOvVaw1WScKS3NSObKItUiCtt3hc",
            "snippet": "Get offers from dealers and sell your car fast with Quick Offer ...",
        },
        {
            "position": 3,
            "title": "Advanced Search",
            "link": "https://www.cars.com/for-sale/advanced-search/&sa=U&ved="
            "0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQjBAIIDAC&usg=AOvVaw1dkVfLmYm2-w9gRoOAKVh0",
            "snippet": "Advanced search allows you to filter 4.9 million new & used cars ...",
        },
        {
            "position": 4,
            "title": "Sedans",
            "link": "https://www.cars.com/research/sedan/&sa=U&ved="
            "0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQjBAIIjAF&usg=AOvVaw1M6fPsd1ivUlHj6nFr5yi_",
            "snippet": "2019 Toyota Camry- 2019 Dodge Charger- 2019 Honda Civic- ...",
        },
        {
            "position": 5,
            "title": "Research",
            "link": "https://www.cars.com/research/&sa=U&ved="
            "0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQjBAIJDAD&usg=AOvVaw1AaC1_Gv_JYHTPHUMSeZ10",
            "snippet": "Start your research for your next car by comparing popular ...",
        },
        {
            "position": 6,
            "title": "SUV or Crossovers",
            "link": "https://www.cars.com/research/suv/&sa=U&ved="
            "0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQjBAIJjAG&usg=AOvVaw2W9RNOoIMBl82mbBTxeeIp",
            "snippet": "2019 Jeep Grand Cherokee- 2019 Jeep Cherokee- 2019 BMW X5",
        },
        {
            "position": 7,
            "title": "News for cars",
            "link": "?q=cars&hl=en&gl=us&ie=UTF-8&prmd=ivns&source=univ&"
            "tbm=nws&tbo=u&sa=X&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQqAIIKQ",
            "snippet": "After kick-starting the electric car market in America with its "
            "high-priced luxury vehicles, Tesla has been attempting to transition to the mass...",
        },
        {
            "position": 8,
            "title": "Images for cars",
            "link": "?q=cars&hl=en&gl=us&ie=UTF-8&prmd=ivns&tbm=isch&"
            "tbo=u&source=univ&sa=X&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQsAQIUg",
            "snippet": "Search for new and used cars at carmax.com. Use our car search or"
            "research makes and models with customer reviews, expert reviews, and more.",
        },
        {
            "position": 9,
            "title": "Used Cars for Sale - CarMax",
            "link": "https://www.carmax.com/cars"
            "&sa=U&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQFghcMBE&usg=AOvVaw1SvonetHYi-LqDrRlyNce_",
            "snippet": "Search new car listings to find the best local deals. We analyze millions of used cars daily.",
        },
        {
            "position": 10,
            "title": "New Cars For Sale. Find new cars in your area. - CarGurus",
            "link": "https://www.cargurus.com/Cars/new/"
            "&sa=U&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQFghiMBI&usg=AOvVaw2QxLkhvaBOsIjZqaImsFh4",
            "snippet": "A hot-shot race-car named Lightning McQueen gets waylaid in "
            "Radiator Springs, where he finds the true meaning of friendship and family. ..."
            "John Lasseter, Joe Ranft (co-director) ... Star race car Lightning McQueen"
            "and his pal Mater head overseas to compete in the World Grand Prix race.",
        },
        {
            "position": 11,
            "title": "Cars (2006) - IMDb",
            "link": "https://www.imdb.com/title/tt0317219/&sa=U&ved="
            "0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQFghoMBM&usg=AOvVaw0Ro2X2ojHvAr5TyRD1c4lM",
            "snippet": "Find new cars and used cars for sale at Autotrader. With millions of cars,"
            "find your next car at the most complete auto classifieds site online.",
        },
        {
            "position": 12,
            "title": "Search for Cars For Sale Online - Find a Car at Autotrader",
            "link": "https://www.autotrader.com/cars-for-sale/"
            "&sa=U&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQFghuMBQ&usg=AOvVaw0ojI6n7YzzoPb9tEVzUFTv",
            "snippet": "",
        },
    ],
    "related_searches": [
        {
            "query": "cars for sale",
            "link": "/search?hl=en&gl=us&ie=UTF-8&q=cars+for+sale&sa=X&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQ1QIIdCgA",
        },
        {
            "query": "cars for sale near me",
            "link": "/search?hl=en&gl=us&ie=UTF-8&q=cars+for+sale+near+me"
            "&sa=X&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQ1QIIdSgB",
        },
        {
            "query": "used cars",
            "link": "/search?hl=en&gl=us&ie=UTF-8&q=used+cars&sa=X&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQ1QIIdigC",
        },
        {
            "query": "cars movie",
            "link": "/search?hl=en&gl=us&ie=UTF-8&q=cars+movie&sa=X&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQ1QIIdygD",
        },
        {
            "query": "used cars for sale",
            "link": "/search?hl=en&gl=us&ie=UTF-8&q=used+cars+for+sale&"
            "sa=X&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQ1QIIeCgE",
        },
        {
            "query": "cool cars",
            "link": "/search?hl=en&gl=us&ie=UTF-8&q=cool+cars&sa=X&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQ1QIIeSgF",
        },
        {
            "query": "new cars",
            "link": "/search?hl=en&gl=us&ie=UTF-8&q=new+cars&sa=X&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQ1QIIeigG",
        },
        {
            "query": "car guru",
            "link": "/search?hl=en&gl=us&ie=UTF-8&q=car+guru&sa=X&ved=0ahUKEwjerbjYpv3fAhUG2VQKHQV5AKUQ1QIIeygH",
        },
    ],
    "pagination": {},
}
