# GATE-15 KERNEL 1 — W-B2 COMPLETION (see driver docstring below).
# Self-contained Kaggle kernel (CPU session, Internet OFF). Launch is
# the parent agent's action; results are provisional until re-judged
# at home in a fresh process. pip pins (home venv versions):
#   mpmath==1.3.0 sympy==1.14.0 numpy==2.5.5 scipy==1.18.1
import base64, json, os, zlib

def _load(lit):
    return json.loads(zlib.decompress(base64.b85decode(lit.encode())).decode())

def _text(lit):
    return zlib.decompress(base64.b85decode(lit.encode())).decode()

FUNC_HOME = _load("""c-rlnO^;K_6^8fx3adBC48f|ZQ=f^l=t*|4h(IulD6u-U0Z+h2wjnbb&417H*1a~}?p89UJ&-}M=x%fEI#uUA@A;~#AMZ`h{&DgApD)*|cgxGO-%ozLH<_HhaJ)Nn)7GkUu^7Lvzgn|YQ?q6<<>p(qv)}cBei+!lRBKK?hMQv%n?oo$MRV0z8OH{VeJ~E@Wv#gstljb|A*RIO?6WIz9B)_V?yr!F_h$Y!3BFiPEu<Q22w{-$va9Wppdlf77aH=b6>FiUz*2pUzO-0k@)lhxe3HYc{7ZjTf!dtQA(jwQ%E+lM=8}q;1&_pnywY+hxm2d8G3HT9xUNR@If9li0G$%Em*8C%cs{wzdMt)gFhxRNL)s|kPZATST6ee=f!l2G&6|&g;NIjXM4UZ(ID0yK>Sxc8^H+)7<59spVy#vTrK30WH_Ofy=aW#1E=Kb{Viq6T&L~=oIO9XM%1R^4h``357F`R#S%ggWR+5X!c|Q!?O&l5F!Cv2U!TFj+=mKWUlvtB*yia{0JSYWK{?=7_JgD+C%%07j`Kt<PeXfE=5(+FU@v60WSXn(nVoSm|85R!>>7z0%XBwlA7NDIsMm6A!kUhxG406Q)2{mejouQ4&3^tp#pa0rTIc?cPmQZuVlyI`_Ju$f!EoYZ&%o#KK5OUe$2j<gMF_(jJE#Px`80TXlFcibLGGLYl9+rjV2k4f2?4DYOZ}u$g5F7xEP6okbIY&&7hqTa=CTUI_H|z_9G1kJ8M<<7q(`FvV!yyF%>66e5Wrmo<qADsy#^WE&=e;(BsyM|)zGzMlt6>lR1@bvy{E+a>%-6ga%EJ%PqjN28%BS8phs$}0TJa44fL(w`EW#7u1cbD4vFM2dMXxX8BE_)0Fvk2T1|mW6r828k;smDP!<a@rlTAxW5u}aDAw<+%tQc?4RgTUg0m8|r@UHZMD6m*WNthj0nK{A?QxZ@4L8h<3jHF8Babn@lYOfc|+4I$Mv)$|x!J~&`FdBqEdVKKT<?jEZ_n-US$nW00c{_W2J(QV9(g7x(;Iq-=HyM|~1}=)9Rna71e}x=$9p)KiEqBq?%T9^UK>@447=@(9Gkgu($ZtxHCHbHfRoWQbo;WvKy`QgV7q8#Gx)@U&5g{}mBhlF7ZW)>oYKTVFHKJpIB67wC_PnX`l0n*Hxt)DC-$RA&W9TI4_fSTD!lkjlDNbMy3_{Fd#a8fiSD=l&ZLs)=-G~+oGD52>Np!M+#T#K7Ju?vkR`EECjA&fC!|a3{BvEDrEhr9s0(^-Y!wbb&S>_@1<R3w+6-YQHQv}_}rtpkx&Y~RNFUmn%3_t?P@*9GPbaV~VR5ArBjH13d%qarW6gMz-5eP-mpZ8e7WByhRY^vXlzm`|K+XYK}!$ED2%K<mIn!teD&G)Pjtpp^xF^?eTAhDVZquhxLLp^ei;ACx4mH~QDGDT)9u6l(BSl($qIeR?A{C!n~*Fu89`~4xi6*Ezn=t&?0tda+IpN%5s-yewR5$zyJQ$J)C4+K}@QmNzM<$eKj2$dF&O2)$zT$;)zqC0_rLV*~N!G*L)iIJ<SkzJ5M%5DvEgv4mRQAmTROkG6WMQ_NZY{F9vMqETN-bQE&d#?|(?fTvF`NejzTJ8eC{Pk<M_YF7Q1qK;n_IAGB*#e#`GA1H9QBl#bLemo9c#I?ks{}2T1Oe(MNI$qAVjf-<Gf)GKmFiLt4Mgl-{!uQd%!^8<_#RAmdQ1k}F-*p|B8xbJ`^Lk%)vNx&efD+dzB0AFnC0~~rLIJPgjNe~K?#D3A%o~kfFt=dKGlcNnChj8VFSgw2s`?99Llggcxg*E<}EJldEx1`9*=U9JL8R*DaX#cs48z)9{)^~5tPBi?v8R$WI`K)rG6<U#U2XVA<Rc|lhVBrFz74DL7pIpj-=`6ay%L}T#GD>i#wI16sfV-fjl|_G%*voF5Mk85*)orB9r3!O3BqL8Bt~&g659n8gWm#2t}1(sqaV`l_Cv4JldlPr&P+3z70E&IACw@^Rhd}q18wbnd6;NBRMoB6IAKtSQOEk8U%~w5VfPY7E}ZKtWphmlx|rrMR!3nd8~)xikQ@TZX(@N@n+UZszc%tWb0fbDxUy0H9A$gP_Rbnr@aD}N`@Iw+oxM{iU0UqLVK0feyVh)^CKS^0Q9Eu28R2lQ7s4bpukZbT2=WAD;f)QSEWz6qjrrB&XbzP^7|@;55kltgLs3I#2m^2d<o7|Wn_vIoE|&DVQmb6w5c1PKS<$7k98`)gqc$TLbs7r%wnQupE#R*KAfWpT8bW+&y++|>f>Z;Q|TsEx5thj)CFulIw{WeZrSAXp=L>4v?EXIcQfq^$O)U|p{!~13jZ_(9cn}WOQPm}HDsekCM`-gZ7NZ<GdH1>K8pf~_N-}>$!p6%C0<VLq_EkY63S<#8{e@4UYV3%h=c0+Xu&9^GU+NSC1~r0HiTA{C7u+wcr&GhPn%N6o2~EQYWqTkPsk4DG$g6JR3cTAr2;k4Orp|F6#X;=qiIOw^w<ieXO#NL^8`6cXQvK{ww{&|KURHtLKJg|zk-x<G|u5RoJ~nuJ0n3`?3L2ox{v2<YW1D<W<^^fMn0iXJ|WIj$)7%_oPwThN`+qox<+zK4Ou%*=8_|55G-iDD~{h(R2rhGPAjn4sbDMVGbEMM&`swmxu1Jzcb5s3L9|~K)#T)=&0ZEmh|Db#L{IA0K7WR!aw0d)G$h&{(gBJ#9B@{O8Y)3m*&yI`RHRMMta7`QQ{v|AW>T?FnpC8`vO#S~%j5xCPzpKWmKY{D)WU&Dwal!!{)bNQzn`?)^|Pfz2m=$+4b$vLG7)-!RP7CH)!wK!YITmsIvkC=<MID~I{Cs7{y!y;1k8Q86idGlVqY%D%1IHs*MIs6%9GjRa=zRywm<BSPoB8l+0c=%@r39}KQv3zqH|CSrn>|zRQDY+c()8_nUzt`hCohh>i=~Sf&@7p?>^}VW;S&-=wK-Lq`Mg<p`^wn+BNK1rERUA@+*fz60UYdgngtI?Zb)k>~eAOa=F?p_NUV4rt_xx?9yiQ@85>MyjtA(ta3aNL-M!hv$yNTay!42@b!GN84k4$<iie{{-BEtR4!3>5OlMopZL+4QKCVCpbfs1C{S!K|8nu-#e6+qKA&r<H;d)FP1ok&@>8d|EETKkhjLmv<W_McvU^8S6KECi6Kq3ozQ5|QTy49wZy%ihW-}R;nVj3?kCWdDEW7XZ$MX}uI(L)%!{cy2>gnHk<|n9rvAo<&wyXV^yc=`B_U{>E|1jCUnoqQR-YnLalgs&f@&01Fct4-4UPwwG{ncc#xjFY0In&9X_pq?c__aRKukbY=UOn@i{cEv(HJE=mqQ2t+=w2koxGK=J;iWTK!c#IDJ<~NR!i|A?4KBxC9qQ_pjxxqWU4)D>H`@zP|5$mgUAy^kyV4(d4dR;2>sqHCj+<_{H0{Y~+q&r}p=w_XPw~3uq(>PyXP&**JD~?^4+3>pt?9xKtuk5?3U&X0(Cf9osI#G}s{z`190YE*t2O@je6`%JSFdkg{fPa-$-STc4SGO;1O""")
SRC_HOME = _load("""c-p<3J#%EqaYg<46%(+v9rgVoQ;rOI3Q3MahC<wk4N6)WT#vE;UFRe)KzE}b1`W(|mmC5h-s`HY%$qlFX3bx}e0})S&%gfT!{2}X>zA)zA2MG&q*HqMJHIP_w@>5oyXtqfoyzJnx9|M9AD?MHvwY!~ufOw?hyVS*KmGid^H1{&Kl1tOuMdCz`M1A3fA{s_U-|mqAHV+k@DuOipH^l{eT=!r%wwjy`^t6A)K{vd&$-i_Yt2~2`GfK7$bHqEQ%}2>mgnrdwwc=ERb`fv*6MY?JljsQj$YO%d#&C5Kz^_1UU;;u#G`xUQu5C~<$C_us$;LbY8^H0oZ1{YPd;<;&0M*$g!1^<czAs3Kc1d`__y<2KdybG+<G0Wq@MZsRCZpxu$DGzE^KJeocr0jpSL_xVX1YcGHdJk(SWP%)>|4oWnMbQ>K9uctEJx4tck6y&R+L!gAMoQt_#o9v|`6sOaGT&Ua!6HT`=)jth=|d_TmSn@`{2b62`2JljsMFXP=vAS<6~^=aF{f*_k=x#agg``?iYspWh!}^YCB4{O7N~{`^1Z?(`2&E`Gm3AO6Wl&mE~ZcC%N{E0>W*#cO)0E#=K?XJbp1eLg?`&%eEVcE+NcJ+$rz`$%$kb9)k4h9BU;wVyrw>)F!-o8;xgyQjST^iu0CyQDoAe%A2V`t1J?zx?*g%hUHB#>0P~KOO(%r1xVkq6vR!s|~_tmb@#mf!zinvG<c(|NiCqOngaw=RbEr0@2ktj@j4)=g0ST&s{SCOZ@Q%Zofuv<rXIJa0LxGJFE$afC{@e43c{7INZh}HRBC05BF0U#6G}-xe1ZYfn(1+Hh<zfYd21{_DP7e^T#UdEcgyj?#%}j0+7&}qmS8Z^G5_~<FWY;P)NE9uD~g_uJ^V|Q0KxP*iPSxBT0FVc_XrTmaWYM9Bpt<ldm{L0CH430%PvcuXdeu`hkB}@r><G{h;o)!;_b;-+S!(9l*dEx^|v}P{C(_7j{5M*4lBdn!4zkRy|mM5fXYMkc$v2BH)oEq0WJ^y*$PTkl}8tUSk6eWhTKlIO<BY?y|7!F1#4vYQRe62l*y8@MfUJY?jO&iBF6D@wUb$tM4%I@@;Sc4{$(sj}LbqPUIWXBe>0W_8e@aldpQcjShF8$PIW%Ihz+ZIVPJXSWF?=5DslFBBqm!$SEz~#E1L1z~|V&AI%5)$N0c{Pw0Pw5&XfNpua2hKf?;%%L_QS4}||`slg}7!Ds2gX9>a&p$P9K3F{^Xq&u@e53B|@@tJ9vqC~60d0`}CYS#iL0TX-QMgblNoY?ag@u^`j9Omb&8*jn}ZDV}`;yfN?0JD?+P1=Lc9D*$Hz72<giTL5(!SBx=!xaipz`+7pd0R6PP`t-e1+fM}wd1k<E*MB6t00RBI9NZLH*@Tpl(V!4#)l8(n{mX`1`3CSbAv!zTd*K(h_jJ;aQ8(@x~Oal454lIOziU|sUNr2wQv(Q4}7qWS#DJ}x1j){wWS;*W6_4MrJZn-+!_uvwbbzSeID<DwMa#<BMwI1ZGmRBfeM==S`B{qAuzbxzOUf`lfv_Qub31BF|JuDe{k^Abc+jZBJ~IlFsPXupvH^43~ho-Y&0*<rjf0|Jjvt{An;2A8^ct|Kb+YBfV#&GIRPw9adMP(L<;Udpl^_{Pg%-4#4C(I>LlHoX=V-1>p6i2dB0G`Yb>~z5PX&r{L!Rfeuxy5^gcBB6fO9JiNSm)8hnl#{K4el2hf906NJxGgwK<NkJE&FdY^u94GCYK4k@I`k4c9C!c>I-wh10Th<cThi#-c(yRBm8z6lL%_py4R{Ke_PJRGZr?LDxJCr~dQ!3uB!=3!WDf}bolJEpJfIH!onk0!_P@_0Q>mi3s1l?Qh44ANQYWL<F>gy_8J7U{kP51h<2eJ$<X#qdrVYL;g}4wW>}W{$fRS2N0KPS=m5zJ?(1`Mp{YQxpQ`6nJYKg=E%GsG&)e3JqXzS7<N}K|U5W`P`J>g%Fqwi?j00N7u+r{ENR*=T^LqvtVuK!pnK^%Fn74YwG=kFzJ298BksKQH_SVK7tMRn)ekl5I&_S4&Ws00OCPVW=*ED1(2C|OTUJNmp3dpkaT4bj=WA$idtKqAS|0rpn4Sb*Rb&XhDv_K*#LAfibyDYWS3xc83_OC1cdtmD%^WAuPcWvrV=6q>gKGP@T%<$F0u((sU)4{Z>TNe-Z<+fzfYVUhydbY7)pzaTt^I&x&i-#;zD@A^lDRV0$c}o*^I|anoJZf10uP~5gRd=EPRTW41o%&2n@kPB8!+Ow9a{HlTYM6(l$AJndexWiBLLXAq1nJdc^AA#f|5clo7aYnS=x66rnP(h6H6}19hvN%I)x9JG3Lhd`kiWT`~)<g;Cj^xJKMzh%*!PlW?3PWvdy%a&atdN1aDr!GaL+3;@5k3E}g=6=%g3qDGM<NXaP@$Y6Nrh|oL0Z%evrf+sb#toBQ+Vql!3NP7s?Oht5`;P_$tz9to9U<(apZmkM^v^=YF-$fX+cE#}*_W6oZ;88ndX+9frKPNPVH4%ou7KSG&%XY>gc8KyYpRD|ix3hwwgsebrkwSTZ`DQ)GuPaV*?+JZ_k8?ZZsMI$3-52b>8)ZO!JUU31<a#La{}Ay}sHO6i4^+z_D$zcR^)tqViGh|Ry?hkg<W#Y;S+9aB&9DI9<wYC?PYxMLIV;_NDkpxlNC(Y=j01;p!YU}@^hU|&CWY<jJk)b4AyJ%wI39v;xpW{5G}Aa1^Hp#e^}FrJm%Wo2)TG&TG+X@eOx9Z?*&V1ZA1>Jr_C9RVG&=`N*<o2j0&C&K73^X$wnECq-kXH7$u*+WldbyUKYSv;D_D?j@znQYLX<3^IaC*)r95XL7W;i!<l#mX3#{f`|2W@8v9tx!NSG0McmeMSpw0v&F=t54`Y}+r*TOd{4N@kL=_sTLxlaj7+3hNX28FL__d`^Oss?vj(Jq3k4k9qrsxI3}xDu7_exuGXQ9(=yMA*nu=b*$~A%#$bQzdW!qaBtR_a4wKOyDIsMdPI4a9KT&N64el9DZH}Z)KwX!_-Ki94MqPo~As&Sy+Yp*!rWyuvxhK5iCHEAlV!|n5z~+4uB+7zN!)j5oan;oIO5IB>blGAcXLLgMp9##cEmNF%=%ix@<^Nicxm;VwDb4)EE}AHCqfes#?ig3NU#mDp2DP(yA{2npp(zfQH)n8J2YdTAcgQ-XRANY5A^-ShF<7@A)}LB!%1>v0ZGvk409YRs~4q6Kpq`MnZ?M$c1_JJGzqLv>4bAt~T*VTlh>4F_FmIid}keKEicbf78WCpT$~y5d&oP<eS(U%Y>BAkHNy-Ccc3S))A}<eoY=x6XBTg$_C*eOPXx)Unsz_0KqO(R}HLKUPeiBDS!>xY?`DS=p|1-1O_9!!&O)^ph?lN>^oc8vivfFx+V+cLuk17lx{);WF?1)AM*j!)&x%wuBxs=`~n+O#p}n2lNMJp_sm{xQeeUnLO@81EmJ4JxYkjl0;4Nts}S;snp=~uDFi=Ok4ub&xLu@8YOilp8`mLw;x=ovU|CZc7lMV$USflkp+eVi+9A%$Gzg|G1s`^EH8ZX~zB{aNv3tcr&KJf(;(^@4V8Fwo`&73B_v`Cu_k%jtK$kFqtF9jl!guz5Y^GF?Ze8uZ*t%i&q%wOpSkNjpCs39sa9%*c?hbf}E;w+L%v@8ulLw6mJjfzz@j<*i9qofSfyTgfMPCrYxEldpCWvIUq_Xl+e7M)jw-ibP0@B=x9~HtCFN%g5{@R>-A>>m%Rw!W{K1yWv@+c4`-v~Db)T>(_B*L@0_Xa``iym+jW;nSZFQL}4I!eE=o3;2G8s(h_brT|zv6_08A>b>}AwHf|t1_}e!HnqG^QKx^Kdx5Vdn#7XPPM?7fksk#qpnbJ^mMH5(gBfxLs&oB_@FeU2sE3{0#PN9tGrt@DTl#^g%ve{3f$4x73F_Cmpo>@3J!S2mkfP_L*wya9{aHPiO~w2V{VUfI9T*v#S(0Xm-u*$uRug4k?QXb=YW>hxgNqT;Q`-ps!6B!tVaZWgqROz>QPulJ=84WL|Hj4E5G4CeFap=6v>z*9l{9seCN0W?x$=~IkN$=TJks&xNJ@Mb@mE-&V!9$)a)S5V~Ut6%|ngRv`Z$iW=tP!XxwYzS7;$ul|!n_D3dJSQ=x3+99ao`dx3N92r4!q3Wo`SxjBhuUQ|{m<d)NNwo1=r^(&l!%kz37kZcdjo*^a2f+Y6<E&Pi;9<qpg&*jFjLsim(k+JevH2ED5*`Z)=2c3inUi!DxER~Bg7*)e(WeUSAM-8z<x*8<KB>y^^i0Iv9I&A5KGwgu$FY3d?%?gS%#PPl$;uKkSSBr##WTu_~*WETPKn+}j=&K`N@(iED;44Zbo2!&f3iCUdyKOw&pUhG79Yllu@|L~j%2W_+)Uh>txA<f-dFke0{}K3A>kjHgTfv0_inQr8LAJOjS%<D|6@9snkOQD_wnKG0_79&cs^P4t+FJuZ-ajK{&0u%TB9f;uJE5UiM95RXFFSxX1`aX2Iu4tc9meI{o|^iS<D0}B0l=_|2p?n`cboava6~jbRl=0EBN8bjiUS<k-Z2*QcMc^A$`-w?+PmATi_<ch%r;{(0iva1zYZme9G_|lnUp&5yQV%M@+j6z{z(P<xC*)Rh;C0yQE&wOtx=-~zoL+jIoqiSivxl}<A<o0CX^L3At_8YL%Sy09YiwM;S_TzZy)v~c5J&#5vj6QnbvJiVNuXI`C9E3UQmmAS}{eVawLglpPa5kH2@8WX*C&7UCvGV+_HKPDcDYTgEbE)lyH-x5@iPk0RHaa<oW*X_U#%Xk}B4)RiavM9;+O^^SbqXz~E~C!_qX0paI&cOOXU^2J~9wY@h?7Q7-mjVO?=jo1xG)P_4lrAR$)nPeMCH@(y&cx#Vbz6Wf3l;ce%TPi9ZX4l8oNq_y(KMnraJ)s~t>HkOH6PbgAjca&y*6dvxi^Q}rGJ7XXCVtZVbp*h-+?W5shu&^4s+Obq2bQ?vb+PiN<e_8q{u#qGejtSN`3K7AdSV<A-*f&O<IO8Tv$a#oT5>`I0L+(DP=R%~M$Rw-BEO`>7{OvC37&=gQoN!-g-k+8)J-1@tLMpd*5NSRPXk>|YEA3KHYuEGm$fu#EuNnpOg6i9Vw8H?~UXVgngyr1FWn;p)us1s7CN(O<5$w--F|f!t*|8Y;a*)#JY-*RN=AE0W)xu^5d7CkiVSN{@VZRp_+_-}H1mECoMz+~ZVw>F3V-vDn2ozbJB$}Jfl~vu9w1FLfYZbO2J$7GTZQQ~WZdj};!vnjuGH$LO1|ZbvBkVioDCM(!(sc03xUx|Yllyiin?r)2Zk~K#zS@Da914Ko5eGdD+H4Z97QLnkQu29Q<z6JX+p<qkz}mpl=I|h#mFS}YUTmnV<&e4TY^V;bbL+kqBh18RI;Bx6CU&RD?x2Tq7Vg!QOzK-|B~^f<T_82&7dtyyA;ZPtox`#T57NA$McjWj=O94tg9=rfUAx3^GS!A@h%-~uA@9r|IYg<=WC2t|F?*04Z5pAtl7yF%2M1uc`ofcD)O*f;q-a$+$+(12ODp?!1jks{B|tq<CQ&M3<SEEu+89Fy+)T63OKe9Sbu~Z9b3?9YaaCnX4nh<K5w#wp%GR9G_}u}@tDQGlzv9XkgO>D6?T8d2XOc#f9<O$eVXPwYRVfh%tS)X5k!^iB6zEm2*E<KsNs!CCHgW>%Ak5&@C=Vz!I6pJ*nV&S@C=nSgq}U|=)ZsY7=&9&?Hd!wws@;O4J$3?&ldPzvSH*<tj;mEf%HH{0DZLv9?l$f-5Wq;BE3#aVR9x+B+9`Ixh|Jtc78Et-27V0$DO-g3Y?DL=TUR`{E4ozHVC^=-)*Dce9KYTGkm|Y0q?3f!*xvi&E!E3#yS}8WTUc=S2|a@WiGzJQP3(H*A@H`f;+7gEc8?JiyBRM`@=B6ypO7TI6e(3KP<>TVZ*q~v6k^R+mip?<^PnWnu`)YzhILbKa?oK}G*~S;Y7e^Si%}qcJ!{sOvKSK&eH@rppeiv&kewj7O0fBqJ8)Dg)U1^lmmR<)uOL+IdF~jZ9Pb{Vd=i^*9nq<U)Kzkf^!Jzv^CX5-uQwINY)L6JO~>l=Us4!P%6bI!4$SIS=d;z;#a=XV$`icxh6$@q&KSftsEHiUzGL9QH<+iqUPu5e2X12qxp6Z1b2C8OuD7><C3n<c*<!7jH@7_~hfp}ZrkYUZ_}FCiz1DqQE##P}#y&egMbmOnWIDPx<Ep6I+&Z{<$!DkSE}ZNGRUD5|%qlU91J8Eej?WlJS1*e$Roz34DdNZnEcuZcc%gVWW_<_?_nyryDZ$IRO*yrP(w|7!+o93vH6AZ~I3U9r{Y}M48!?zLZpKE}(>obXW$eg)WkpQ{D?3&kG@tWaUWnMqTd5Wa&iM~zgz0UTR?hQTI}N)h#G18-d}69E$Fx3a)%hZI<65p1hka53;;?NGd3lvwXzjxnj>HbLG$)zMJ&FSv&bbCkJ`;?+@%Y{;Mp@32lCiHV1h_+4PV+%~!M)*Nh6<I11wc#XURE@2FQ4nq5IQSS<IWJ?DEMJ4`!B_QGhv#_U6ln@l^a+3k;ga%i$g}Ma?MAlw;^?Qf(3R~g?i_GY{l98YgPf-ATus3D(9!_ihJ#PQ(~CKcFOi18>BIY>RBgv)V<cANVYZpA+0DDZdkR;nWj>QDo|X8ul7t$&R)enzM#e8yAtY>kYs6zeG6sK;Y67&Ovhl~U=;VB&o}UJs?KZe(!SvBa4h?xxEV>xA@nUHuZIG|$7+kxLo2my?=?E-GX=~TXOIbyO7^^LEjpetR*%0i0n*6gNQUH0?;mC*XV}N=ueuAxxfFh7i2*T)X2#tPS~zy-s6DvfuS$!2Qq*<&bUsc@P@~}(&B-3n#)%5G^B61Ica#=Dm-F7;ZU?(}z@2r&_%fM%0B(Fty=tn$_J++@F(B*Fw#4|(t2bU{ppy3f%+=1v2_rddmf<;^CXNx;l&l$xf1^N-TUssOTUt18)9rD2ClPyCs5J9xmAO*d#w6yY!jQbiW<3^>X+g6jkK$Rfj>Y4gVESZfai?*gumINrLB>{+9P$^rXd}sF?}Ef_A&kc_e5bT<7SWcorAQP{+o4?ZcGJv?hhD>YbK=3_;Q)AQFsB{tM=0}|aJrS?uyk2(R~C03(D}uz=5?&@1pzCYV9Abi>0}|HP?fIsk~co8HEMDvKdm>X+VHfE+?@PdcHCE}4?y8nYMUpQ<b6teEjCS@YnEbBOJ*;xIqtw4uGGSOV#hOmD;%94;Y>Lz?_pt}7TkzHikyBSFzn?BL})FGv#?U+EAK-(zGAJ<hkHXazl{QHnbhQ1n|Dd#uYuV%0Vw^vQ81idD&8`GwdEF98M{NBq`4R_A2FogNlW(c70%jzwdEQ2Ufp!HNK-FgQEb@MTH)(G<i+)N^ygDd62%o&Ys_W;g&Krti`#$TvF)-~hgAij90HJPSykc@wRp;F?rNSE;d!0&koQIXhm83Y?ih3{qFa297&gF@tk<IrXwz3e@41{C^hUUov|C*4v74iJMWNw{3xVszshw5=YP=;SI4*$kyr<yk{`UTZ<F3M%T?Z9#c<tHU?q9wI>jw_ySwrAyd$tbCPPJ60f$(W>jM?k&y?dAJF}uyrNs6Ef+*7CRF?BedXnq`-&rWv1H$=F7tqGRXRK{P1H92CcuQ~V#Czo6~1m#7@b(Ob=Dprgic-xKr&!{&5(`9)^{p8J*WS_01i*Tt!&|lfRJh0P77O^Q)#1<a%rv8X!mhyI_yJNV5g;J|2N*%ncJ9^<%gE!Otiv;HD4G#rryNK!%k;m*$vE~p;oD_AW>(!1~r1OwtPc0f(`&$6LV;fE+XtR9t7WrkQx075*=b=uU&aSK&!gExYG(dSussA((e%bu-@5!=(;SjIwK9woOv{1%@8wH$|FJ?vG7wI1{=5t=xpx!6}*v;?T-nQ8}hS8$5_wTA0=LUTW^aknT2&}qEQQg0<iQlz;B&9DaLZ|!drIP(Ez{@GiQt={XE+xh8b#X@pw}ZA@hb)(Z)wj6*&=EYxbw3Ff%S(O^z44*aApo(Prn)12aV`FZw7y7#U--}O{|^|~x{C""")
BASIS_JETS = _load("""c-qySTaP5kk)7Y?R}}h%GeCDL{O-=hya?I{Nq`_gJKP6h)hNyshrR5}Y+pzb-2Lx5pJi2Mm}f*+WsxgL!@jXHBQwI??sn|>U%t6{@&3cdceiife7gPo=EM6JzrK0#-@d$k`{|e4AMb8{_wmEKn}2-uAH&VZ4_`jty$UzKeEjhC!~37_e!BVe=TD#S-rd}OzWE<-etvg*^X-5CKEJ&Auiy8VH$UIKztaVuZhrjo`6k@Gsy83r>l6O;>h52@ym|ZPw;yjm^8tUnef#OVzq|SE?WZ@N^z!H9Pe0uJ=l}HT`1Sg-f4=*X+xm3#?U&cf;qc{kdU^9l{`E)x^(X%Ir`PG`!|!fB{doIU*Z;%qpWlA?c=O|jyWjop&5v*H-hcjdy2tNsZa?1LeE9hJ_aBZA{qpAX?H}H}|M}+g@9%Ct-F^PdC;as0-QD|7$1nZ#;q4c`|Hf|U*Ee@>-!9*`m;4>R4~zXH^2qu-ec!)3@Q?48n{V&F)4%TC9lu^*s%NtA{rSWD+qXBLKiD_EzkSCO|8o2O@9es8zZUxS>6f=}KHt1~uXo<w<X5_<n_s?synFTY?U$dmFt;B+-+cSy+uKjN$J_5-+Nb^f>!5G`>CRUF_QyZ#Y2W{(tE*kj9sSFf51(0)!_D8{{`mWc8|3SL_eQt%_RlvT@9vjT-}~jg?%>_+|GxRx%QgMin-71y`*`z*@3sD2%fv;x_{R?)f4cigtMFg$K7ac4%?~es_?3Ry?_a(A&CB2D5B=jGet-A*_W0+o*qe`9$z@>=d5qI7+~3~In;*XY_}%xPzPx+=hnp|@{q46OUva^A|H1zJUw=5fcquV{_u;3zPZHn1d~<X2f_=LG_sxsbhQ5B-&eyh`dP93@?|AdmYm-L(<bU#mo8>V4f9d7+&*SCKdmFX3`R8E?y@XNy&udup_7X=q{k$wWh0%HnrN!PKey)G!*!80l`e?c4;|uYy^d*Iy>xhd!t4K)$ul&>T$?jg8NSz+cRzyFyHGX~ji^S~iC%qaDSszn!X{m%b+QS3iy!dRJ|JpYHVSVj|A5I^t|6VNzZAPzslvdKHCB@UC-M>6isw0ga>QZ{n>(}C_sZ~8fTXM{yo?g>SrD>74aM33&dG%5VWkjuNN{c>v$;EwL9bM}YwY*JRQp4&(eaXlr<Wx(|z35MOWz0)hVn`z`C50N(`qHrE9!qUu=+kqr_b>g^!+T!*W?Gi4Pg!DLw8?tR7}iga0$Z$Si>dXv1h*(H23^#3eJ(wQ^8>sJhh_c7q{m5F52;ToEtK^aXg4KMNuQNdOU+%DQq*sKi56HJ?=I74hMGo5`pg*oWldWZQ`FLG(c8lU9RL2e2eJ9*yU(w0KfgA+J4?;ih2_N$zkHO&^1gBKGIRH8DXX{r!h6a=Vj~&oB`-bq6!oUIe$y`|-V*IvC0Z$mHgc4nEW_>D*S6}#Zys*R?tI?1x_Y18le8(bd$rePgqkBab$*wbzT=1apRK;-emTEcE$Y7RO44;p`o3CwTTbHqMBPQIqa->-txH95#<r|!^JN%f(NdQoiz9pC1a^_GmKckKqxJ{WW!E)~oMgE!s9Sb&m|K&<DUxvsa9&>(N61}9K1&s~!Oom$Ri*Wk9&LMwF|KvAg)B=UBPt!wDfdTpRGXf1)mJsy5`<~}O+zcQ)K+9iWPrS$WJz$xLN$Izcb%+*1VoRN^Qbb=?lXI;UAospY+C!ZP0&|J?`r9_jMTgh)#lc+)D(h*^W=Q&GOerDJfpb!)+M^jYK%+Ep@gQ@O3zW*ugJ(sU(t>*DQG+JD4|Iaq%v}ATl)DbA7YYF1=%YZgpksfe(rA5SwD}aW!kb?KdZcNz*5Fk^xN!8`}fmM*@+r*<nE;(EkDDv%G=1`j;tk={*1MWmoJjpYH}V$fk7Ormuk|YhoJDF$c+`RbxB4%$mfo(Pc41z<O)7BnsLtBbni8ai8WHYD1OQ7>-2d|PpRKkPb_tI3LAqQkoL9*Jla_6kwji$jP70zRr1>&S6F<46ksSE8m-2)0_hu~mME7}q<AH|2h$QsQ?iy!O5q-?u&_;kl#Y0%JrgLy*Z3Wpls`6S0d+gNq1<KBy1rq(O+#)+rqQB~Az$V%t8zM88hK(xU(fZZdqQ$nP*aXQfw|Y$aEPp6)E@GAx?$(L9uzieorgY1-zp7LD7LAvd)qWQ)V(dc*Vk~6wn`iom}bmuDSw?iUB$<if}K|L#ZSLIe$-#CRZ(qW)a?yISeY-k^LsD-|9aWiwUhVjt%{1|zZ5<P@A#CtC{AnAkVT)nwpJFWA}g|2OYzY>8l$92ZhevaaW}4*M?qMXKhUqq%j$wi0IQ@zIn_F}kONkfl7oIKbL1U2&Ouk@Vv2m0YRTd9Jl)(|-AOa2x79h+RiIb!zp~jSE9hxknptGYT2#O#BM=p3#0$mT-=PaXy0cp+z0`g*g@f9hD7QTR7E$htpMJi5_wITnWZ&u%v~6us8kxQI9c6HvWl<(I!f^TCVm?Pwr;8O*);zzeq*!63)=N2P3;%Ck`-sb&QpO<zuTWCkw#X`{;WAtkFQv}>Ly{PM`rFC2yW-a+bt&WeMSWJ1#n&6;LL`8}znD590FpwnB26z^Oj}1LISbRrCOKx(n<eqjF~1s?q`XZbR_OY_&x&sMWM|e;Cr9y8L1QN~iZV!DA%baWzwn(&fxPre*>jK=R%q6!+IZ)=+OP|)+}XT)txS3tMcev@q^By`-NLh#@(<7Pie<NE;cGR2_5XRyB}qIKsYFF=@&mb5ZyJ`K7lph<u}WV{yP{FWK)OgG7G<`ZS3$xfSz*0HO4@v}OX8>)FvyE6(ijRjr<b!5B4xH!wpo^3VdA=~p>!!#<&uirr9_g%u(qj)jx<x5P3VfktAe?8>OvJy;#67-5@*Gd#fl-%^I7GI`Q59q86U0%?C5m%_F#$yr~OEibdQ7LKjjKT35a}Q`&*=LFOD_mH}8MGTF8BFpuO%rcFKynHCeQmQx-RfgqNt@X-WpY9ixiZ$gQ%LsEqEf-F@}{>ZOnAnOls1kAFWyme-c_B+C8ZHY$u+h>vy}S17Ti&aAY_=Q#J09+g$ff-5gxsywo?#|vY=Y}s=E!(X<f_S&3=KWs_pe}t#>Kf<!p012q#`oH_&<jFseI}MYu^Ye>_iCmXF{q%Oy+SU}d7x!~3ND?E|^ZS)6gi5uc%d>}5A4OStQ#P4fQ5cxhLybZyCb_$!o>3{>rG9ps+Tl=ASH#^YV9L~Mhtn#Fw5Hr^E%WO)wzPCn^ZKQS<z2mgT;|*lB`JT_uM%T^sHcW{h#^$jzmTx<50$R0fSYVZNphtGn;veyhuD*qLlv4ROTM@{>jJ&Dj^XRuCv<~i>%Hkw^*?=MxUOWC4&0txm_n-77AxjeXLS}@H`+;MDzwFv(fgORHzO#5=?Ndue5|N_h}Jig7cDr+)2mvxLPT8aBGHN2yViQp6Dj0s^4L{>7x(HhwvwbMPL)P?R6c|@-L~#DQ^{0-E9tttyiw}ZR$?;Aj2<<ZNk%AZHG<-~K!CfBKXMo)Qq942R3Ei$Y1J{-8FK$=ku3Mxr=AkGhyp0;l)&&;o1ZW%F&s)P8fzcNd^LSYxvxZzaw)6zA*>-@s#H29gw3yRI8?=>xy4BTAQCiOF3vwri=*|_HdFjp=s=fXUFXx%5s8<gMblR%SBaE>(dp5;QfYUUa=dVeiZOIGh1t_f#hMDag`Ro(*1dp4U0ErhlRf98{M<ibJCO6_6jK|>h`+iYDviY^cT@F-Ublo#A1<}2<TJHu{h#6OzN&j?{}&FE0@k@Ke{3v~&dD4qBvs;-HyvO*R2iuf^;wz9i9RXB+5hc|`4s(4B7e3E_dasBk+v@?-ft@R@=|ja#3z^YvvNeKh~oQjDq~;OCyx?>h3p|&4l$(;G9ofP$NKz8qh7qMyQX3+12q&Q&p{^nh7wS1zg97ab?zX;*T@}5lHDwmhQ`CdylE%LSm?t0*YC|^mRXhLNN$v2q&iD5@lUA|?^+ec_cWVNEq>MWEff~oc)WQYbjwlCOChhcvR9N}FxOSdSS^IAt}Fqrpa<zI&5W}zJ2@hf5gDXJhb&##yAhiLV7ccZi|@PSi!F9pYNk^jl#{HY=X}uHskF;m)h?Sdn?pU4gp_8w?N@u;AaX~jtW0Q5RE5fL>!0Pj0#%1fnJ`QU3)$pF@sTuH598d7J`Zd_ZOR*E|3+TRL;<-HEl8GLP6knOihwF^X<Z4ebMy6(Y3JnyN0H>R{Q?Z^lq5l_su$Z)4=)#2o7!Y~8XK3M4K>))w^eEz4wKf!?TjERxG11a<N!mBb;}~Ys!Dd3g52?FJztu{ugLaP?g<w~*Vg4^B1T@Gt(VOV_-nG_4dQWyX4$#IBE|y&>X4fSUy+yk42zho@0;k#=A?*j3R-Xo@~J_AjbfVF>L{g_K^!p>G50B}mc`3MMvuTl;fegvN`6yUye1h-it19xvx+KO)Z;XnGv(@SO!l%Ix}u%YF_n5p_sSs$8_^uar+C;hN1N@CsM1S<bW2I5V^jZUdnl8k$V@qFr+DbYn#NPIRt5X&YFs#xPR}#RoK5BLW~Io`l|w0@jrB4h)}k#uqhjhl@}#43w;*pU*^*Lpw?0<?3UpdqvF?Bi#uet1i^*Q+Wm+DkV>xm|(u-~t<0qNNVWna#vc&b1cxR#bQ#qb;LwPxEyL)2AL>;V@wo_7A`bt<Rf@m?Qa_i=%_$|p$)<tHDT`zs9b#|_`1A`dS*dc!~xr2O20LruvM9{H#Q>vw`(lFUy>3v#q&+FB=)*9~W+R7Tn!=!Or#;_bDE)`r>N{VTBsv}AlI<Kch%RFsa!ab>;V#8U&=h(1;1Z%{X3f)V$6n@h(Zi~r=SqxVNhWapRf}*oUfool!g`l+l0`Y670n?|Z4`GfBt&;L!Ahr2rd2rx~aiNs4Qq`eoL-C1%zF=s&F)N#VRHyAott3yftF#EAQ<S8QL<YTVDnyVrC=ykmpnsJq@e7BnfKi)*g+!avtT-}FN)M!KGSqU<PqKq#VA5hT%>uZ^g=GPYTqJMOZSYdfVMeq3d~T^WfO!){MKPW<xUt0ec4zFBQtB=jO8qhn-dAMMEfIt(aIP@DswI+P0Eud79B?C39Hq}}LC!{T)|lgRx!0kTTDPW`6!cqM@^wo%<3mvyh4qT1sH?1F@?gu?5Ge`AQhfOrU}gmlvtTb*ZdVcmMn*a6pp6yh2bN`E!)2&|PHVZn$OLey!=eqztfKEW30&3QC{s>dNu4%o7C7y_?ul->HRApnW4NnuD`VIXUhCpUs;p<S%8=}7pe$n1z_{$q%fMADKuXZ0%oGx5Yq%@hXLA@1lZZQweMpt{NmQaTMQO!HQ;Pp!55r!C`M5rl@Wir*q`3xZuDA#A7{KgwLVR8UwvnsM6bL~F*OYg=j0^i!fCDzHR~S=z7XW%GqL;%r({_%hlq&}S5`gEV+GPq372C+2DgW22<lvjtoDS%&^0#7!66fqj?pLX!o+QdB^fcG$BGp`3g(8az03beEN(8k|)r(k98Rt^{HwOHj<NzO{U}U=8Kv^tFqvQv$M$@$jrTmR@HEycRQKDjR`4>`Uh0?wp$*UGeDhk$4NR8%t2bC(Bf5jRS=dy+kbcNu_cAF~xm}`pZ5R}ekCMKx*_G35n>$Wig(rW+^f$fH#FKW|~B3}bvv5=e2$wri;1A8-wSJD&?N4=(Ow`1SvDy;-&p{FZ(q(r>rJZHmt46r{k3U#zHTwC`c5)ag+<z!_<6v4zfTUPdyz(NJKAkN~5JpphGkP7GaOeE8e>OI;dKG5W#<B~~5)99PXhz2r+l&h2QhqhHp+!yn;ft-Zh#jn44fH0DGHH9bGhLSzz_`yDYRbafuRFLmQ=j^JV4CKcQ5$PI$>uSqb!4r^{CLCj4*SaJfjl#Tiw5K(~Z?c)vKnbYw48v@Xu(pYEm-yujiZ?HLic@4efCfo7(sGe4-;1zTMwU;`jUv<vn_HzH)MQH?0QYD8kRhNlj9sGbRh|?i761Z;GTZ>q<kCEY=aALcVn}f}9i%Ow5*D}&ckZ8}$t_d+Nl9L#4wuCdOjSefBLdOKdFenAvL&MIM8o)^fgnFoi6Zi#nmC7n0i4~?uBJdCZ?+(^NJ_Glg)0T<^$GRF3?90Gb0im%+`0gPnSw|%A>ELtD!%!m5I89+EvaJEyYs7ZXAId?iYro@yq2JpsE67!EMv+A$V22_5(93sf^{yL<O7%&#SYSGIqkBf2|2@f1XUirOJ*i-2_S_aJyWefw3q%oBe<t!6Ig6d<L+%@+{Dcc(Dy*m0%mRyI)`Nr5qBhe28zv6eu<@7*dBbW6uVnf?h-2Ybuqa>B`nJ%Hsz{XVx-dC8Qjrb=T@#AWg<W~5TYFAG8M?_Y>?Jz$wn>?d@ONOh-PW396|JO;GI_MI8gNNw1K2|y`>F-V<?T*R8b(<TAE*`XI4QOH|Doymo8_Xlwbiv4!n1|Sl+9&q@*R%Ph6e=%+5%E0Q*l&??;OyEHd^%aXtfbu7Oe{8y#?^UhIpzEZNARH8iOxt^1t{e62DnJ10vYHx?(N$u<f_4`Fl%WRn;TYE{&z(y?E>vLl@lsn{iriYiOmioYZEBE74~mEv#mBjv*ad@Iv*0FpVvl(b^kw1I^oH=>X1pn{3Unk0`oR{0HAm{F9%q60anF?$*PvUJKKxVHGhtqDN_VMvuWmUY46_$uLX!|Cz`?V=#0Y;|F{f|`cb*<Y-PQ<o?~q7S1?@>$5)J%yVh!evkSPQ7M^{FclbwgqY0G>>Ig$1QaGj+oEpaT57_(P*K^UnG6fE#1{pH+#=tmz%AW`a+Jb3K1LA$(c?k(?<RJX)<keruZUfsW2n@MnPmU$cDZ$CB)(fk{2?U1V~z|+rN@_D=%X{wh|jC<e6L41*f#|dT8}Rrez8wQL>oHMh(kFW-RC5nNg=;9O`N&{1uaZozW{|ld<eXK^I+So{HMKyy@_XI%ZkQ3Fb7@ba&Hk3RZ{|D?_F&_{MT;3~g(jyR^5@69@XjDj~JIXFN2lOSP;S&50!UGM7usA=u<?z?5*m7nMfql~F8QNVX;n3Ilry^b>Q}c|0B?7KOA_Pw4nlu9%@*kp?y;iYz%+X5b2lO7>-b60str0&WdJ_YE4$dQ`o~_tgUiq6C}LY$x#E=|u%pbXSWqMW6=L(pKwKOMpA|?mpEbjxjqbulvn0UHa5vlc<t$1+UKqPw(p36e8~G+c|Hhpr~k52}#IsLTsAFx;f6iBi0vfm2DBfH-lMu9W%~)O=*R6ZhKnxtAer-B+i1<t}}u`X@~rK9-X_2*G7p{oalMjgOygCox>p)aDovQgyak)h;+q!+7B|lsZkA}s^fKGZK#uQDKln^6{s1S+Rc3H^T>=PZ?!T1=yFvoL8d&(5T*3qm7JJ0(E=*%X}aS&$B4{;)Jir)QzSk<SS#NY8Jkx;roYQtd6)%jRJA%|n7#>5^UfOS%%!h~9VVC#4^lyIX7Y(N)kGEHz!8ub1JZ*9|1eQ*SkGIP)PPQOa7eiuS<_lc3_CpwcV#Ysc8k6dh(H>TnLJ&v*bL(6%UmHezKzC)1<<+Vl5QHCI%Wnh01C>}BUFiiZXOV`A~r|Uu`n~Ggjhn;`})zWD<x|pbE!a1QlDK1J|tjrF-5~-`p|r_8k!;)Kni55Zs1xOdZ&&lKi!m+KP&Xx)uK7}n>A|go}>e~BuqlF0@&E(2!O;xyN?ZLKC+k1nd3bPo`Hrt(!8SZ=t@HwWy^A1vge!8-&ciYv!CLH=NhvItW^%L(K!M;)#BCJu~MZ@GPl6AQ`-dZ1v@9TTL?=_cFCxoEh_3`EL?6Vd;7Eug)FqSv=FH{CILk&Q8wDhc%q-_%`5|ntx_jGAi2q_PD2vmlr{00YNi0#m8i>nSZQPZeGJ7lu$l6f%M(IBI^|XFmHq=obI(dZgdzDxsewg%d!#5+$vO3^B#Ra2@lE-LXh29BD&1S8O6);*6?TxtwM!bURy>Q1L3<{W4zf`~Z8SE;PqE<~puaIW9G<}Cv5tr`xQsp|xsfrK0gqh|hEa1eK%N_BGxKV>e+Fl%w^Rp8G7uVQ|I|inZqPI`RHr>opwp%&m6?#i!c{6Ut&S^#(jxJamXxV(Z!0sk3ixEGQIG2AqDqpmQF|@chAGcuLD^HFmB}jyuSXlKMZwVE5-P>UR4n_Z!K*Y)$j~K8vgRRf)dF`V_-ydXVG`txZn3_Mt~Co3*-0B6>>J&XuL;X!@Z!OX%`r9JYapM;l<r<XFx5fUvL0%RPZ?_JPa<{8Cmfvnxs1&NO~vWwkb(pV1N_jD1Wl$*5t;iOYIc%NB=`I|WQi#l=&YZBOJvklk*}OOP|@-LJ|NbS$21-?8MLl<<cIm6$OsFyB6f-N?m-{|@tNYLN(c#CT0Os}*c>*OFd*7urbjQGJ`q}<#ki6>TB?`Iv%30v;<8w`JP?{+%|QkFS`r2Qj~*iIM3B+=rIf&h-X!!>y-O+%s0843GnX_sb|cFzA4WlTjxHI^Q0AD8Ov2}!$|4uqD@xEhqwfyZ&L~Krqd>4g;O{<H8>uT~jDP{x6Qt}bqsrv9q)?TnxEqWzm}#&tDS&{Tq1ESS+^ihZ#@tS$2q|ZykZ-w2iuGW$DV9d1b#Bi`f^j%ylv7jh@C!2xZq{MS!{7Rak(pGu)(SCOtlnuToh_962HaWl0*?*@l|iPnWP@HWu1`gg`3V1Idf3(V17jYbJQpL!nx~<n!67@Ep+KWg1$ZVXf&v#=1m*>&`R|AqFE~HSQN4MdgaI)j9D3T2mK>$wVj&UJgaZtd$Dl1>GbN=GU#RHf^CI&dW%AXBxk-PFW#t_ehy%?}n@&j{fScB)b{Z7m`Y*;^_hfjc{n?S{6M$)94lmiXw9<ppcZR+9L}R1uFpJ7{-T6q2TLHpYOYHjSy9B98Il_wY>Jv3i4UGLu>e4y@n`g|AgIf%Of>d5+;(=!TX*NZlN=-A*hOU=y8Ag0rr;v7`>Pp8YO1hK0mRA=LQ3`u#Wa%^V)Tv1Hpp;QDf0O7(JZ9-COsNJPDzZMq<-^idnVqJ^sM9hf=5c_$ftD#_(pX65WOS&4=5Z0lazQsj8!dEh)5=iEO#zgXv~Q{^GTjiVkx6j!GS>|Q1#ckE1O?;+(@ix9QwSjzh7lgKbZ{pc{-a`hoJ~S(>=`kw#MXXg2pOy*Q9&q7&&Nbvg((z_`?wgQfLbZ@4D^eZ3kDXpgH(*#Ma=W!$n|IA6O&-2bg?)J^%Y-0stQJWTAZc9grTV3&?e6f%l9;EE=BBU*+acG?old%Hwb2|<SxpF&D)XYnL2cm?AhkMYS1?g#>SXN4?E*M`$Do|^Jbx`*EQq^RZBfHoFhG657sRBUFba(0CnH}tfY95-tl*IEPm8SAm~zTg0IP*{1bXXg@6qCjxpxWZ?}{jPFM@SrtVW|AalU{T9;(fRfT{FZY=GO^nB8x0e2qcDzu*BJcSgghN0@rhla;XtpFwA2-5pQ>5HQ$W4eogQ4!}<^5r6^i8~gz$LQCE$xxc+R63`KOAcQ)E~3CkuEEK1C{s0>G^Rt~%AHEH5F;A=sL_0z9TGKfe0_u&c&;5JBI{_geDs1I9pix<pfaSv?2#7LF?q?x>KOoHg8AG<u@UAfXVy*2mMv3<k;WaQJ_)vI#wF%7LeXGI48TaeN}ep1(g+2_3AQ<^wf<G0aTORV9NuN_UB;T(HX37zw#zed>w7vi8@oOII+b0uUo@a)Nf>>cjLjL8DY1`@;gbapj<HpS*p=p)-e*U$&y;dX&71Xgfr)SRkxpN@EhHNja1xp;gT4%qg}L$~kr-DSK&-FA)6Aq4*vjP7SpYN{&|k@8nnlB5(mzxVb-^Y?Z?emlX{7=GO#M^%65(%?&#la=yVOJ;sxC%w!BCD*p|Pyp+Bmre;su}b$aBh1E1+QrZOS5<EXMXicTI)vaRUffL`g702a;3QX9E(>ltd43K>Olgq@59X4%!zf?T5-#B@=lRQ(1uK+(KlMts*&NJ~G!SaSs4BCGD8JmZzjx9-?VS3!Td}0m$Jg1)bMqDzrgQuy;&P!Y>mCeAhm)FR+{d9&cua{ZO~$g0?Z>_gH;cra%|^OKf1D;ry_mlx!Vzjvw$XMM(w0u|8FHa7?^r0sh*UbRp>XI5X#y_BPysjeBKpb{p|=1G}j8Y#~3-_U)?E)LNfa>mt<4he$Bi8Ev6880)6>D+emQMm%lA+y+g)>^kkq^4x6Sk?V66mW~GWyNVPk+U(6R?#j%D`I}|v3j3E1i?IpPd}T(uUz_v7Z44D2EMic{co79_4c!a{Vo$U>Q8P1w#K>5oXE$XZlv<1(lA>OnxGWcfJjfCiw@-c^7tScKu~ya;FLGh|Pr%3vlx;o)ptqV7#e?juTPi*yFTs-^kroy7javmXoP=bNkz?1@QIJ5vmZxhz%+=mo1xh!L&7FDM=oB-*2QYKQi#jL>JdpHqDruU2Nfp3ARgMp8Fib|V06~O$ik8+y@TvW!T4-aSko`QC=Z*m~R;sDJcWj|7N@CQxL+C00>pEl%P_vSdyf84}Rwcs)Pz*${tl3EcPIY*XlJQZLa>+L#hskUMabHu!IFH{9xUK=d6~#=;T;)}U%M@#{2VbU$@ffc&fIFZJPtRj0-BF~A1lK85coOJ5F&`Yj?=oIQ19A&ixg*0D^rSoTe2VZaQGjVAu+}?-K6}Ek)l+xEavhoy7C`bSMG}E{^LjKTEIXV&!s!*g`z~-q+K%%iv`1YU(i057GFi|=jJDVBz}qs>F_;1llVBMHsTx`qFk9#sc?^>#%#(lxN%I^_W0zoj(WlQ=b%6p~?pkpjgAB`fbo@{`I)!}Bb?LYzmyR_9Ni?SR3#Wa!wzljBjKc#?p&2wI)oF~=$p6C7=RTBgq~BAaAZSw*RxN6S#(UUY+*~8zu$V@PL5ncItlRIPgK6k2GouKAbxRNBdF46kV`eTgWGbat5;R-Y1w|PWpvt^2*!t>oNoFWyZ9AdvlG}t)BY1C6Z!Ba$e&_LA;H0Fh3bx`Dh5<^*MiodjHtjpF$rR!UplhBRYyo1M!t5j6>v@LM=F=meTrv&QXM!j9RBASLvwB_fmsP67fJ`!Fo6VC9>V~P?mF3yi&2qf~BeIiWNShe&9JTG(yIm>Si05XhxvrqcoQBZ?k*c@rXAFyR^h&1&@s_J~18RW}OUnif)OQzXizoAr$5WWr7beJx6+TPrtaac~mB9iIfCQiz96Vdum+S_#3ROA9GN&W$Sn-bldaLh=4)R>Ml53{p<rF9$;~)dCFkJEYDPIg@ffw$HLn=~mxDzt4Q5X>E6I@y8p;<m%O0Lo!OASCk!Zd{xWx@|->#GG&e7bu-$P}RfVM+ih84uvs=0x(cO6Rjp#|MGZA=a%l5xhABNrNjkzOM9G1#jk>r>jma1LR}$WlqSEV8yAlK|Od}J4YoPjtC0aYvT@836jEe5w_Z&briHNASn$(;XE$bml2I|sbxPJ))?dGxDtiU$>9c|^#Ierpbh)<Ory4^HB;8Qt3eN0YoquFfe>wJrKOuCyLf=ZjN{#u1CKP1Ha|=e?#S$vvhK<6*~Ed;$HK`NbM)3WQt}a=iCIdn!bNgCLSgzC!qbw^rLw2DW{rFk?nB6Gl%!7;HHJ9~hCCE&0Zxe|ARvfNKp8||9p}`oV30m~&r{<tAF&bCkcxuk?lHPXAQz$KlPpiL3}Q0UwAA3L@nGm~oP5;2W#mG3`ca{+CoyD(I6Z+>g1|CTD<W$ubBL+vqNF2!VxTC#kOUSJBKM|fsg^00fGeddx9iv>kMXnWO|YeuYvr@2Ace7;0C8HigAXV6A86Y+*rj*8xOWNder%{g(zIIBM`4opdG%nFMQg|s=8eYFVsvN#ki%S*t@2cKIt%5oHg}i{Bf6s-_8o&ituy$^!9k9h?&7oyV4<}f1;Wqd&Y?RlNQ9V)=8NLN>00eA+QU#9z^D0WzG5RCHngTSdtPsLU$xH04>CQcU|WP^@lXxs3L#u05~y1w5`&2er4(|YN@)W$V3&OCyJEeH@bY02?hO(NSP!6K9olf9Q#O;{H|ZF6g=aE{{V++<nbc$rnq0#o)87sjIZh|dxSx|m_UY%~DWFZ9&a_noM=9aN%YFPgyFodr*3-uW@n-fZG9*^c=t|~7C~;&nfalwxkWwM<2CrX0@jmdg+j%s@y26VQCp`40GEgMCVAcT-W7W7<WImcfIrtM+&@(C$msTP9jG#o9{#;aKgyogvJmf#M={;OsJ!Pz-a%4u~Ag1i<2W0h1(i^aw;UW38F=fE$f<;eLb~q@fN>&$ZR(rEd4nmxijkjy@gxdq!hJpd*Xx-uy?tbJOW-V#G`>#B*wadmZvFuOlq&sP$J=nwgIBe)E)aRTa2&fRyUTt}5UJXUd0JoI2Y2~KAS4u_^oU$}D`D4UvP!&!J261|F;kFIoW7H#%xHc726_F^QhU5xqn##`{HXxG>41~&}OZ{bRIW?0KgkBHv@lq=Bpu`_iG2hSOyd<NgQ!YWJe761_#ycSRazJ5j_8_#0B0}bb*;!Hw^Y^72r-^^^L~|EhXQoV$rm|J1`oJ+#g`uGdO;nCmWUZW?UR1rPDE`)pGkVLs+w&aKo>EPr_@08Dxqu0*Iq{bE1EXg<c*z1!INjQ8!?%}=9{VyqH_vzE`ymvU7wwp2*e46Dw>xJ)?TO1)>wFTQ>!{LoDU{rW4pPj|U<PiCRMM%|uQ9bbnlZFOK3Z*{aQ}d8I8`$Tf^fKllPFvR0-TK&(i<&+{LunbJFQ}hxvZ40%g9^+HLR-=kqJP9RI?cqZkU227zd`^GW30q89bV*AjlaI?0vWan*|~P3QuO}TbTGPTM95*G6+}Wd_cN1lLOhvq7}oqBB7BB7;OfT$V4#@nF*P+Tx6c3*lvw+jxEWYMC=zuY6n7*vG?T5ydbR>de!t|<(>Lt1`jeqT>_3SQK5EA(vP|;3)&4t=GTNgk!}H`dy6+|`XFYZBj=D35tnIAK(RxSYQpH(gcBo@cA-^B`^J1yn9<keW>aadmZ4>7(Be~V>a|Rj7f!mN3m-W>PZIUap82jC%@x%>mHH|?QtCDu#JltpC8}Yoq`E7_ZcNF`^46GA0w;YOcr5`%+dBblPeQznD~Cx~t~?GRQY*~hOuEfpTs`%o(3e^b6hezX6p_Qh<u&XCYpw4j8B!#WHcWp>-;($Fz@xPfy;BoylY^zmGUy7yk0A;3!59^V4%Kw6ov_@uNMU8t)e5Fzq?s@=;H2zeZmBUbqVJk4imaGRg7dO1k9N$NwUJUN(^KG)qPH{T{{}2<^o)E-71D^sK;m>E9JvV)pd)vibuWCZ)3cpkp~$sSTARW#1|6VTvJ)or1bjF8UMTh%hPjxZfe}*=0({bV@%*wtk*<ixXg7NdkJ&vSpH?}6dvacs!r^*_V_jSIC6lkj%y?)Uw+sWG;koil#2o3?O1We9g#`v+=xGE6ht&^T9$^^~_Xa;fo(NE)9mHVSi9Wmg*>pR*#!j=MO|W7uxNZbyN3*6VZ_=`Gi4tO%z({?mG#yWkx*+zoqgBAKC+5eF1ckE&+?D7{UZQR3J{Md$V-+4kKw8V#I}>L|R<^3Iv+P_I<$*s`kfAtH@}2Va5b?zn7Q{_!19-eU!=5lCE!K?-^Bfgu?Z#nF@Q8Uk(5jKq2E0X{D~Rj_;4fI16wJ7m5@**gk+z?dI!*}i20KBc1ka>r_o(zvH$TAuY6Lz$df?13#*>1P<US4$k8t}zIW3`!X-pMoeO0ov7ltv;y9zIb3u<V_Ar#v_P1BJ{XfRC8K!h9I=7eYhu|U;s_`yEIh|p%TI+iaeQgk&&2rDft9$Hw9%Z+^wR089p71xOM$S`dtj{BNGH=SG&(vc|h>=8NDxQGG6=P;oZhtX`n6iH&@?cHcL(|nwW&B+I9%nb|<Ue&KLW%{}R#|WSdg0ra{(~XAKjw4H9eMp9_2?r^|J`SOOcxHgNr$I9%rPrppyVMT_AC-+=Tmrs*d~rS)7kXljDr+74R&!}jd{@Q}^o^6^t$2^42#LwbRwLx;We*U(Co7Y^;}CTxHrIxH=>X)G=&9RCZ@apv2f(@#neo5rpnJysnVH40M%PaP;*$r5J`egSzO$=jEEvxZq@-zLdXWcD^hG)9e#!weVBc<2ziIA}+mH-%&$4)a*iUvi9?$%sag}_2n;Hj$cPJg2Vw&-IJx^N0F<44bF&lem?g4jVW`<+|1nRrK@QC15Q@=PMoI~e2+)9u}rwO<>0KP$MF6Eqtj7~(wk-0$XcTR7W|MQ&y;fLH$oYnxU8&0n36l3xe>USt6Lx$iNy+knONF|YawPTrMG!~|T0n{n`FkcS?EVx1_B_;GVgK8DYz<d;>;$=$jJJ4x{GbkI(_#oh>bXu7U56P2#*f5`ht_-ql!X!~&g@&KwQOK_I^J;fHx^szw+}5M>$%Yv#4%`#E$n7(%^P#~$VuUKNCG{;-<c{<{dWu(P&;qVGNr=*hyo-a}l#I<5x|fuzVmR3bDuTf2NaL<17Bbq5MzTpB6dWc9=2Hq@#-uqWZY!9{&@;xA)`8d@tjM@^hBXME$#*>%&gwGxIC$W*XvP_6X+T|@CG`^oJZD(P46!`iJncRH4iL^_Pz&X^kFyE2VbdQ9nTix^3fgEr3~QhO%67~S)F2_%uSWRmDtycWSRqkCMlJ3oQ15{Qaw+glqz)av=1P893?k_si~;UO0?&j<pXfQEB}z73WCuRfc~H0pJGR0O?b3%lKHX9kYDn+1@qs7bfyf3YG)Or_{k~gI`=EqqqoBIq?15hmE)SruGz*%K;AwMP31iGX8TwGNc$6V23r{wR1JIZWVzzdf(3nIsP_n>HK4wZ&c&~B>#HNfy!R@n*+l~@lK!m(PZ8RqOFm9x1&8)c1rnX5Lxhudcb5;(M9B+heobK4jIysO+snqTvg}cJBc}U?TEZ1>HQo1pBj7FVj7oN@;36~y#G`3hVm<K765^_36vL50(QXnRWAQq0lyheH-k7lxl4(K;v*#7kA-b{dvQQc3Hroc(%3iV;i^|-;v*~}b&Jm_eI;4?QRhI+p>bFv%mq7bCFL(a@>b$`4qq5M+H6mkcjPrTr{vhBDR&a|_0t%@IMV?eoR!y!oZ7n%udoS#5l#up%Ei+~?OWdmf*gSO#<%SIShC_x6tsm9;}$(_xnB%cko0(M+(1x7yK+XZ?L4ILn+T%KU+m<{iCLb+1o;R+cUj6*&i@hsJKH&Fl@FQje|+q#lNWuS&cT3Jx<-lIs6JETU$V=20{lIgI<S-z#&aVmb`hyfS)G2rb9PdZlomC5k}pq$~FL0jl~oRNE4bOG+((WrYX*A5{5s+~Vphao#QDI=AND7<2DUvD#ht4p-^o*-YKz4wIr-s&ata9AS~ho6P%ps=;o+mn+mu=gZ4*8wA$jgc=S)(?4%@eEuf57QakL=3AhUeJXonFGs6q98Jx+@iTFu&?kMrnzjcfLTAz6!4ZQfuif4nLx;#hVJ4rYSGEgF_o{LhUqvz9oAFM%HybOe`0)t5};vpq2w+TFp_bC9?Fr<zC4bMWXKh`69e`V>6vc9mTeeRIa@u+m(WO7$xX<zmw7gaRM!fO)J~R}=FE<|=G1_}0dalKT0t<|2^@`ct0$HoJw9Nhq!1^DKF@b6^r7nBNKL|eRQ+l2ND^&=D9WV3S!dF72m&J1+o8{NnLzb9BOcHUv<fpZH*r6?CF6+>DSrg21P0z{Tm|;gPirzOi02*Fw@x!F9L%NJSh@`oHIs2!u}~h-Bqw_UQ!BYhY*M4U`CN45o`Rh%Vm!=hwgr#ur02}DgIJVp4BH2?(ulKCnuT2kd%J{3?#i~W-%S#}0g&V*U&aMF;WGdysQUoPJ@J`h!F+IXv=5K`#x?<f<nr1>_Ksl5t)mH(EUk1CzWR3G<KHosYg2jOMS;`;W__q#&j)QD>rAQI(W|uiPpsh<ICAVq9q@@#cD;Ya$i&ICXqoD>PR%tus7w^>av-ScdDhhGdBc!-9k8&X$8fp`&N*#BwgWAgQm?D4$ZDXR92D~??VT^9zNJX5845DrPa55ufVD+L9dtER3mgbCI3xM=DL|5Yw_vpa5LrFGg=7%GLDC&hg1E~5k8H5RaNgZcn<?iH);_@<+aN+~rzFtW)|q}FNdd@k@*nmBGbhP{y>vQ3*Dh(=2<DIAXSpY&H)TGm^0p$cjuPG8{#9Hv4qgh*iPQN=WeEc4NzM(*J*^^$2L*-&8^q*sh-&1x>NTF2|F^ed=AxRmrJmk(I(mTJsbE(EtR83eUKOa8^-orx|INKB+T!i$TL)Iibh}dZw%iNl6ZGxKRMKd-+8H6^6u7S>$0i9=q$N|V)m7Gl2N9N$i84lWVzuNvbWTlWMhZ2_E19C?pvYNr3b^2Wg;EtL7#5~YwRJ1C*Q$YXOjhuWC)le+BAG!rXjeHsq<=-PmT2S?0sf4ookxd`qg8f#9oSULSLX-M1BOCI5BVKe*GP*8xIb$q<h-&2b`n$Kj7Y=#o%L5A4f92@gYDYdu5sd8frBSN{6EeQ2%yOrH#5froq{_X(6X?Mu^6pNx<<`*cYXWx$y27ljWh6}6i?d|E_Dhn5F&(NN25cZc&Sr6+i)@c?zhD2R5f%8lTL|Fab6)t|5h3$Z3fuK-8KT7t2|f$l>tt=!+AW;hL(;2#A(LycV@k&*}T}H)`63X&x4z0gJet<APvxkz4WtFDR?KV!X-QTWMzVj38x(lJvgi8tYa`wf{Tb1l>e!1YgAuBrXSv|fEO8OEg%`_2AU;^yC+`UQ8GIgeHd{M2(+{C)3`4L+C>pqEphc29g45Y@Ro#n^%#(7j%EW`2us>BO)^N7S~xPrfTSxmlueRVfX19=%Xt$9X)4ETXlcP-uP@<TSR-|lUd3xY*Y>tgWyft1IQ3KDjpB3w4sE+XF1b!h7PXdx>?_!uY1nXFJKHex#%^xOIp8eKir!SRT3k1buTipZw1WTke*m9aan=""")
BUILD_INFO = json.loads("""{"built": "2026-11-23", "builder": "gate15/kaggle/build_kernel1.py", "path_rewrite": "/home/hatch/workspace/warp-pilot/gate15/work_b2/ -> g15_home/ (relative), counts per module asserted", "rewrite_counts": {"wb2_kernels.py": 0, "wb2_functionals.py": 1, "wb2_a1_patch.py": 1, "wb2_source.py": 1, "wb2_second.py": 1}, "module_sha256_home_originals": {"wb2_kernels.py": "1e6e5ba0839547b50ba1d258b049187883a9963ae35a38d23eef37d343b78d20", "wb2_functionals.py": "c8e12ebf10730057952abee0a8421317469078f297e3a11f86582625c5160743", "wb2_a1_patch.py": "222c03e874808221d91e828db17ecbc43df7cc94bf6674a03ac7197d7e56a128", "wb2_source.py": "459ef92dc3a1e02c0943a19aadc8e00b80ecb63277ff1ca50bb97f99a722d3c9", "wb2_second.py": "131c97ac87d236c6e40821a1b8b66387e4780a693d03655416f0126f49d1419b"}, "data_sha256": {"wb1_basis_jets.json": "d5546b6577ac1313660069dde344c2118b68af0d57c9e6ea464506bedb3c1b5b", "wb2_functionals_home.json": "13d8b5cac8491fa5042f5042b5ad311c42a61ae6b17f92f14a731fdeaa084b8f", "wb2_source_home.json": "2094a3b29cc82db5f9de83a0dca4077a29e15ff219b0ca2fbc878c423cde5562"}, "pins": {"mpmath": "1.3.0", "sympy": "1.14.0", "numpy": "2.5.5", "scipy": "1.18.1"}}""")
_MODULES = {
    "wb2_kernels.py": """c-oy+!ET%|5WVviQ+lykAPea!(ne~FDpgT$Rda~4kpYvS#XxKmx{C7eoiS`eqRk=Yu-N1Ado%NfS>N|Bqi^XM$iJenpt`nGwP-*zw=&lPs!oHwlVG|*7ZP?-x3V!H+LFw*1|5}B*AK$h57NY*cX9C068f&$Pk09E7Dm{Bh6u7i4I$j)&TLb%;co<~&eQ-a$Z*HT+TMA0qN$>~wenVK#2TeGJap7L1oD8QlT}q0wQQ{cvse8d^XRoSrtVtD$+8gCz+>+>Cb5haFkOt&oI%M(zDYuS-}6m6(n8OMjBiSY*Ej3f`*kP{6JZ_}90MP>0`9jtCQzJt0Od)E>79eX116$`9}Y3AG<U|8GqRixr-NdF!V0v<-uGozRL4fBysWEQV$nNLy%LyvHME6wX$tEkl5H7#zVCaL?i5s7%*VCrJ8j{|Z1Cp&R4##a>!%wt?tHBJ%JVXGqWa;B)aqkg<XvN!pP|*~o>$5W%0t%}W~Ek!Q!xO#!Q!RIC%2(K!ooowLV+SW;Yc5MA+D`dhRyfrsVl7FIjmnS^z7sw5t+blNoJ^5=g4@4KG*1k%lKAWhT9O<91ATVm}r+IIegl@%d&DT6WK?YQe?`Hu@&#9G^ImaA0R4Tk!WcL-ICiZ3-$U<QyV+U5<;uQ-&f*Xxr6Ixg>Fa^E!tbj7QVB8EczaMj4kA*=%VDB^JM^6kGnJKmAPy8j4j#-wSNe~pL)&bj&+AN*9(U}c$&rz*^uEHhsqxec9G8`OT*`eX3=Q~DW{q^-k;ONU<rRBI~;jF<42d`M;D!*q~68lTkzxvc!J=R2V$Nc#aw`AIOfJ@_^)r_*YCtm@IgS`!xHQSS1;UC8ejMlew(r+Qo}ao2NEZ^d=SlzQ}iIXrmBaK%|bp8V5CrkGtm?taXZrF#dr3??wmLg9vRUg7%TEdl2Xbc*^W92#|B&T|M}$U{%SM1%~P9V8G}H$#eEPEc-3^mvYc~g)Im_V5OY}mTg-oF%dSLt?;p#5@zw""",
    "wb2_functionals.py": """c-o~|TW{h@5`OouXn7uDCx+M!$($i#B|Njc+LNqKLdKkjD6tIK;0f5QZJ0z+{`-E_7uyhKccqO;rn_!kU0wZEHDj9QpB<mGzeiQv@h%2zwv4hYUa@4G&8jrdqE*Rmt{rwWrr(Us<09R~bCwkOnw7I6s%FcsVSFQUL<%sGXGvbHqZQ+wbzBwcj4h(|Itr_FHILbl&C_UMb#5JYXFKc`gwc8N#4*LtU(>j2jMLdH#RAbPDp;P>I(N2Q`s=bt%PLQj7!F!xw2oPkZ>yL^CHu28a##^}l&{7zE@D=`uBZ7bg~8RUJuny>V>PS8;lLfcJvm`#7~P(*I~v_F>-NNc;x;>H7DS#nyTc4_i9LiF=@#eZzlzH8*S5{(VZkJiT`~51cul)HIk!fvmgyQdX%<It8%|E)E31|<`{y;AMziMyoX_Sgs@Q$HSVu5E^jz1qS(*v4O<YvlVk#oce#BL2Sb-Cq;3Ixdu<FE_oZxd}v!7|Tr2TGQ9TxAR)fR^<Y+tyD<07pPvGryhRZBQET9x^LjXbuF*VDLQvm!6c&TJXao|!dIi+EPCEYDWLcWsWmz(=W&Kel6xII9YzjbumJY?&7hyYHm)IIGg?l?kI=!!%7JU2pQDVn50}(_`T<9bdUI#1TsunPRUu4t^8ESZ})XO^NtkxW*sBcMQyhcM&f0b$tGF%EMOXcFDeJ7@t_D{%ME1p&HY;ieL&WSSIg!eSYbArhO$dS2Mi0!+#^{^9Hd{#18NB-@bggj5}XU+xRLu!rUq4PKWg{P;+6;Hi~<tEY8?4=5fN3aJsMxk(mt1i_^}ScSIW`vBo(okf@S$ig8Ceh2iNbmliiiOln;S)#@F_p{LcA?lI*K$u$;wElsU;Ozm<{t8W;I>#)SbFD`x3LoDRx?*RwOX*t{*>j_TNU$;+j$h`9e`8Jo}g!J3RrLk~{fh7~ySa=wB5;>#rEVv+WO+YAUBZ)_2N$VMlo)GG_gf4{;{i($egG;5VCHn^%r=dq91l{SlSeJxrBL|zI3)D_Vz}E=j86iBQp2K{6F!eFTg{t6Hx#>!yrDcxj^5X7|dd!C$#E=aYQgQ3BE!4J9+rr8YA53@rKz|D<2tkJJAOQjB3RG5kV%$>rMxIU^dFYDUGj7S?h&S9maXp<PGH4@x_5$Oz;X5+y9~kzv;c@)3DHKSb0-R3)%lMZIq{e{G0T#|AnT}4uHD+WET%y%>Xwv|bRhqn7f<~z{AD_>Q0gAyq-o)9wBv`XX4#JP<`;PC~BC{Zl15B&cD+wUmMfHHid732B8qUg=J3nKG3{P<Q5e^rep13aTBi|>sf5fCOO!`Mm7B;q=g=*7u>1gAk3X#fuZ2W$$x#E~mq)uBhz@zB`ytmPSsDE4KQDv1?VI?ju;syN~d50{oX7NK7S1h%~QSVTor*-`U&Z1t>KU{F(?OXK^mtE*(S<&K{1h}SPyc<+g)jmfEV}&Se<=(^@in%9uB#urH#FZS-WmANnc7c)qz9R3W&%QRa6Zdx@4@?mFyTpAI)^L``Nm5$!{B}`Mh6+HbTOw+=+)hi29JU1=N;09rM0(bV7y}+`DO@?swWT!m8bkK*C?;slXbA!#vC^P+f3{~5OW0lEm<2h9d3G%bd);V5*TteDM&X{xMW+k9OD#fTA;Pv=9{pfhse(tc2Wtq$x0eBPg>NslXYck=qwUH9PaJ9AFhrMnO{m`rsY-Q+Jt#EXJ=*NZ&nJd{ilL!m6Wfrz?t!K8z8y*gfvAV}geBFPQA<YVGSNF98qC6vCij4vOq028ms&ihZt#pvk!DEdn`?$#exR7X*iG<mt{)v{il~?(B#pxOxWaf(Vcb^8jw@vQ8X0vlpIEkC$JFktE-^3AXx6=>BlH1<#yF9gwu;u%Iia!DDtM~c6}Y)7<fd!{O@g)mq<L5>$%2k?W8?ShU)k`XQ0GgduwTmw9$Ia0yJ~-8e|<q+PjkhJ@anJ<hq@D+I{sbUW&g;e1P~-dgyr?77sfILV8H|pK#kZ6W#-)S&gfrsoc>zLdmwhE=d`;i;rkQ%;?2<QdR-$5TWzV^<)1%)?)7=!^ZLJCUVQ$1L7nSnUj{v{Q4|LqK~dmPH+h*-CpG+DY-1#`3R;dH422VJN<xFUVs#0+z_%MJEQEeHwlR{P%X=^D^D?!KDRt_!1yuV6p~)v<#PHRIr6n}(LLSWl)(0yTK?Z)m8<bcXo`4RMhnE-V1WU?P3;hwykp~W=LSvae=DwJ7Tfr>p=OkW4*&?=-`WY~<K}QY6EKMLg90IQJ^o;B3tBNnJ-XNuR^C2<c$ierw{M~$PVPPyGj?~0kU=Qfxmu8dZ$TbIy8fSCl(a56_rxB-7k4CrvrcZJUlJiM!L2^FHEl_dBDv8F4Rl7!(ahqFn?_kdN=l+4bFXX8+ALH^U^X(R&ydgh?NTyxL{vRK(-^Zr#?#KEU4z}jJb~w`>XZtQwD7D)QE`@(=*PD>~KDo^f6VX)UOc>D&u}KZ0=q8jZ8zT4Q*#5xHT3i$ilUaXu(3*7IuIpX&yw6_$@}lp3;a~c0uXkaaZ439Vdmg#ceur|aPpvRL9hJQgFos^F^;q9SvF|l~z=Cjv*Brfrz5;4iF#7GuTAiW!v{ru^QWF-0u3(>k6OUE#RF%(4tLUT|+G_g>Mkgc`oF`A5p7>Gy{Sv)_iYxYgDc|32S2RV!HE~*2yjnTzo4Sa&dzg#c*WAoNtS{e}-;TVP8$o(*1O%@^Pu)RR-c`EE#|+{*e1CdMOTzT&DLErxVc#TCPoV{9x^FnV<_NV86CJyhqQ_4y*gGny#=Na0p9wmcbTA42JmGzG)qeZ3T^g}Xk<YiYiWS>cEWZ(24m}Zn@%0fIS~gE)?a)%Zl;vBveh3Q&uNlqL_pE;U^7`pZ!qPvmmad!&t5)C%64V4wg>k|qlWQgoq^PGw`CivIPiK`C45?xBh5>G9z=r`YY0w)6xVMwx1b@8Y1e^&UPPqDp1ug69HN3gDe%J$T>gM{veWYvhU<Lr@Ga`7J;Ask1l!^J+wlv<eG(NO6{$OcbTMD?Q^cvfe(ANa-V708hoQ3&^1+$MUW*?W#>NNwPsKI{uBZd114rUJ*Ee{pxQj@R<!X5FZFjF4arM0iW8Onc330;2Uji}cTO<&^3Z^#6YxsGmF+?qoZx3@O~@3FbY->A2^hdON6#2+AjM3<VqA-5oZ?5@LS(FucXKZ=^{hj@~qv=UWC=o}{Cl6l=?wGvP9e;ssl{84e-D1x6I5y)x@8PSNN<G=>q@GBb*I4?N5W^g(eR0|ORleSDf<Ny@frZ|B|Q8ezE{{D7An3AM`69UM2yaL2hO|ZmJ6obi7VZ3aBOWF2H_z8v(Htxf8{$Fw<5a%Xf_v$0SUj1*#x{qyFzXrA+;y)yg0}5?Nppw9oBLF6ogZ6}Y-#5|zczA)`4*z`}d8*h4`r<rZHu0>A=Ty&+Rt20*5sS`H*fpE)Ly;P9X5y+05ntMviKnNYm~uVkV%pQw-tp8l7uuZoO2%AhbK+|lbD_<NFI~*9YW7vW2TXt6(tei<;O!a)Vc>-mu#Uc9mDpH{1w5RD6Yr?-xDn23>7XYR!U;dFlW8USBF96v6oI?BR=(1^*&&;HK34OrCS=WaL{I)^%5F;|f^77lq?)ijdPWTNZ6Pj55k{-cGSXo>-ofpijH$a>TK4%_>g{%Ni_gyv+wEwdTB@5?@w&9MyA9SrKrJf90$`|#t%(>b)M<%kwQSZF7Lz6<JZw5lh(ug5DBUHZfJzg`csJ;OYPxf5)k0e14Yi3g>yO|&*7!*fPmN?&0b_L2`?JWa7`Fp5w()PWr@8R""",
    "wb2_a1_patch.py": """c-oa#O^>5E5WV|Xl(;M;B#mtdq(^fgTFqfK8uiB^hf#M#H>ATTe5@hqj8^;Kx5_w>MCsj~sA+K3tLIl$#>TR&<zyjlA?A?g$y-@9c>{IQzHX-QkiAw#y=$`u^0LiTUMYAe;XQ9Ru$;udAyAPcg;=ueP^+wI@~VV=1MMb*R_!uKpXE)eo+VUkK!`2iZj%egg``YD;RGse;H5&wykze$Vzu6tuPw49+h+Qssmdw*k+lu%^8|{zNZQRb&DU$N^D@oq4F8oaaW_AU`X{Ig)jCtlvRGc!m1=<~*jiPEi3VdYY8S7y3)||=C1ox&f2!66VrQ(Vr)k~5X9zs@<s06uHy*4uRgv9X6KSy&F<S1nN>aN*W%ieEj>8hP<2<(IO+^@n(icAGel!chFtD6YP!E1iWA$hZ-19t#eZ>(fwAG`-uy8m^U<6;`25b&v_^Pd3o6&^9qoZRq651)yIiVo+I2ujFDPSULBzqot2G!1w17HI3%;%r@#-}k3i#=rSx<8`+W1caIHbaiL*h3p>Jz@mL`^HbXXbg+xN-wJcM>FyhA`=?*p>haa#{Uu6K}r6<sNigeG*lzI#wu{kW=GkW5khv@4E2a+ac0&}VgMi^TTp3u*Ut&;kZVC)3lE(H<Y*A4RAiLeNY3#95{#wU8Xnqwn`U<GqDH)g3k&?iN9Eiyz~3Db#WXd>eS$lhDCTBN(kQ!bDA7&RVoQ3ruah@^oPIXIeNBH)!h8CAoyP^eaZ8O?S-VrES!8#3-P4^iqrn|D<(`(2Hh1N}F`elWzt@Yr%e`FTR%FL=Z*ol^sP^<W+uNjgNfS8S9xHS>sgP$%^oV;>?3o5b{~N<~iWuV#*C=$SWAQ&JNXFrkqFZKi{|g+X<8Z>U(3vdwFH$VJtU3yv$>QTol=_fE>rjqna!z}VJJgNdXzfm6`oI{r&b-ro6Scu1kA7tb`!d$n?9iHRGW~AF+<N+Mbyn-iVcN9nPc!QYp?_%+mSJ9{62Y~=x7xaerd9ovZjW2WD|5Q7hNEpjqmThhRmoIVzGf6w<mIl>bf<890WKyftCkSf<x#5lDB7ULoNioiOlDW2=dn-LXS8wJRPi9i^R@!(q*2Izq?jEk#*q$_4sEsl`P^=Dl|qV#`#x#&eb%4Tv`qtk3w%H;uFy{5_r4IAgg?@|CV@uiv`pGvGgtH#(KREMrcP!dI9GsJ)>GI}eRLRH(<WFyD(J+Udfbz<DBw{vn{nR@r1U~51fR=bF1eUR!khVmhoOh3@|^Q%K0oUFu`6ogye^Pd-UKd`o`qaU?E}s<A0sYA2a<=}p9Maji@EPf8K6ckWEg~V&-b|yp)b)Fd3-+i#XLHSZrV!WN`0-$R#jVM9w-Hmg2?v}`8U&FC@Icur!JU}6c?;_3t!b-e@lJl4%17~Hudk8Ni1(Iw@>>5fr}gcsKPaQ9{rT1jyJ()#lv|)1D5fmr$4P0`v+#izCi""",
    "wb2_source.py": """c-pO4ZExDh7XI#EF>*iD219H^qLwX@nns(dMA}snAQ3Xi3C1|sh8>%<*((2ipEENyh6J{{d#eV|ne+ZKXO6Aw`mk~4vI{>C8qRTt&DL?;$ey!2NLaR9^M`;1KXUFr<k2!^#)?OY&!5@K&*v6PRtcW0Z8xS-80BVD)2^d1Wz&F1Prl%oEjb%bVrFDHR7}kdn}!n(rY<wS9Azd;Cw%Vbti}wEbv_4RYOFxl41+h$leH<<=PZj-md^>`AOU3La}&&84bWKN6ARYqvM-FYb5?SXTTShAn)&(Ptk9pW6BtIuO`(_liA8nOXh>xyVcrY*hzO|wSz|*-SlD~Y1O(Klua@C7lJ(d%33qz*sQ?Xv&9Qsh)NbYhOQLk0!3jhx%AhIW0m2nf%pQU%yML}4)+n4UtU<7^{O@cL@HB`s^0Wy1Q;-pJ_MEIBBAU%0IL#xOkmZatDK?ANsiyMy*V><QKVQQHMO9^nMUn}|><V3{(5(?il;%Om{n+dvQUmUPpTuKhVS?w2;l_2xJaUN!p7HTwq|!5XDM6m_begQeIjnLvHVj`qRs>T99^~wZL9`)+OC3}|y{ZJIx?NH2$E&$ts<apr8)PRtAG@U%G7Qo#s?uHwIhR6U2%!K$fDnphw^|GDwF`e81`G!(&5-7V<x6%oWTDu_F?bAe76(rVvT+$i_i6Mu<LfxcEOzfdEJD6Sq=_igkf9m#0XauAv&p{9{Z!P!Q{=Pn_wHo2PQ{t^<E;6ZAxD?JqsuG&Pgxy&;X3v?j&a1Bny%|wl&qE<`axN&W&QZ5(3Ljh%cMB&3Z1N|0n98>HX3TEIbCIlPTSUoXL#zNb3B<Zli*0#{^;Le2itX~lX0@M2)lHRECrT;X1w&L#&Q*;#)f#;6CL@z?15th^~MiV^q3zAJtNAIe%YJ!Cw*r!&^=GPygER5B?<fPWH1>xk~}>`pOy^$mf)ETTw*&*Y_JiRq}(J+_eMIfx@T&$Lo_oY`Hjt-Lo|*M;~pY$rI^+snih!(4_OmRYr;d;gpQ;+WKKxtX!k+xD<a)(I&JsFadcw!lcYpALBst(yNi|2i_M1HbU%FjcoH-|>ZbNZVuU!{7cOhC78VK?(oBtCD`v;GZA7b04a9AOK(HS%eqE~_Gxm;6$L*sjAGfL5HNG5iI)C6cmeh$^9`FRG$xowfZfd`Oqq3OU7BYlC7k@4MwLR?}9YAp;=`1ff8X;>labDDRd6MZmtc6|2)Gma$5aL3J3tekZ1e;-y8+zE%EvDP3ds4@Phh?%_=K%|0LfA$###SCbca&HMPR?vkqv}nmdeLmcz<{D-(Ur+}1BRGmBc*m`i#ktFyG}=3e~;`wN|%X|T8}saV*|e-NE?rm*ua);c2Ug~B9;XRD{co<NS1w~(j{Q)y})Ghay4iJqS+%|+rNJsJ$iUvd>f_6Ce~!i<Cf9XuVhO{8~)bxSLhB?T+YHv6-w}Tjy(<0X_WuUn~|C%QW|l#eMK6<4~#V|S;E=Kk8uHn!9DlQii}Mw%ryKpY3yl6X%_I@K=OuXrtFN=rV4e6r8lrxZ-~Fo77L#Icp?f)n+_;Nv7g*eea1NwPuIk`#U^<-?^Gy_Np4jLWHZVsGQEMPO^5$o%n)Ke|93H;cjJB;gvbzvh}ANFma!GVUd7Qvl#__95Kn^{`!f!VSYTv<Ml*&n1J%|+xnm$n<%u@8kj@6V-a@z~!l3?;tZOyu6^@CLaknU28_Huv*-~AFtlTAUR|FUIZKAhJHFee^z7N8!>96@^@Ad1o(;MHUk^9_njw_zG4!YvB?TYUwcImuw;{V}=z0V6mw#+?VC@1zA-gfPZlPC7Z=JR;V;L=l&33BQ^RlhWFr5890KVL-KjNfdVL^Fy#kkQCvsAH3?I~#qFZLv`UOpa$tn@`~`Lt_YvKxl6^N!%vrMoW&<q6r`5j5MJugoK}$y&Iz_+w?K!bMB)(5sv0<I?&>#6E|cH2GmvM1K72DIv6cHgI}w2O<~ytrQ!(1WU+}!3m1_J2=yVU2Kq`}70rThs0?fD8lWtl4qw@^ldLz*I+7ObSl3q8^$ta&{Z=$S|4-3ymA*~o3sBrw$^@Bty6KJuj>_RR)xO}oHmj_+-C&6N+_CRi+1FQUBqWHoqP8&zo&fc!%i_&mA)&m0)i`xts}*@ijLRA}VzQ_LBAbhaNklY&m2fG4J0!c>WB^Td0>bT=D6xAd>We~&Xo+%v9R{}b?;X3N7dneAx^}bKR<f_vOCFW1Sl01sjrX}bytotin*gx}k4uDrEau{Blns`<k7NlsN&CWIIo`RZrCLDol$p5xwWMU2o|Ijq#lkE1cP6GJN{z(=noW_E?T`u?^{!|*f=WzbFj<aacMwct7;$bCTo*|oZkdAHUo-i3Gp!YqU#YYh{jQbHSEC=c#o#A3_DN%3`3}U}0)^pN-~OA>H_Y}_0Sr_D3@Qb1TMJeC>&&egx9{=JEo%qk{1M)P!}nt&F}s*Ule!AsV1JBSl^Eqtbuccyxh)6dN=o*5vk~U*6IMi~6!`DL21WJ;o3O*$x+v=0m4r9*{cgHdH-D&$;#Nqa*RY*-b1G&A&^06>w#r00o_cX}Uo*Lasa|0+B#*h_cMJYj$$v91-0M}`gZ8bfOr8nPtd0@W=pi@y-M+;JT@3j*^X|>uVz=E}i`{kaEKxXJ`mw}e?GD9~v~+u7NlmJIA(m9pUHUQQrT?Hl<KU%B#*VaDGRlu5y{~%~JqPM}GuLJ4>4VE)WUGr0z-12*%<t2qPM{+}M}aPZB@2BexxCtDx!PvAk}Q3C2(VR1kYHPas`|xu6yx$L-I1B@2u*jSrc!Jlk4oo~nD&;!baY&3RPc#}U6ro6_{w`TFMM1Su&5?64kW8)_7~pe&JtWMNWBoQaQqrSK-6mT`$Y3tH@E8Gr+%h)*co2UdwBNnyvnh-5{r~pc+J&e1(tLAT&^#~8ow`^7Ob*K9A$Yi9_V({(bdf$CX|*f0U+!WLxA1df`Ich9%Sp7Wc}1>3V@cMS<ca+@Jf&8lWKStd!pk>B+V!f@Lp%Wz^-ID4Km_+sf@oP%oVu7S{7@2#TZRWMvB}Uk>uF)<k(y^0Qg1Rg?pP0a87sSH5>z~+@!nm)u3BqA1Gm!BT*vuSR$SfFKybo`E(LbF5(Pzm>{fv;FD(yhYCmQZ8UvNv^4hCKRSkQGtv3<Ubflv!XdI|u}}#rGDIm7IeM6HGF0-vl&ckw(%jHv-C~HD4yUoguO(%ouv015Vkd`0vst{((82gRFg5WBcDhbhh77R9#HZLl`ZrMVovJQMQ9C((!cqo&=gT~RYS5V4KZ*`Z<N""",
    "wb2_second.py": """c-oCvYg5}w68)}UF{ONn<jBI34VAFVtqS2T*@D`e!r+i{IWE~6OTv2i>S16h{`;Pu8Of4?WL+-3ru+2io}QkTbY1`6KXuu;SMt7dc+AFse);P^XYAYO>#uB;<*W=jE3ztIa$Ea%>hlf9AuU;yY+|0^$}6KRJ!Y#o^U9-<#oWQ5zsVwqoO@MK^e=e;m7KG`E6>lpvchGQvZT_Cv`RLQrp4AgPkCIh`#dU3o-#km`Lc{3*(%Qx!NBLMD2>Qc!HhIxNtR|w<i*U31HQ;TOQVOI#4AJK<(^MtKF^~q=xuqy7LV+cq9u?38Ld`4=jjro*-BW+y?bq$@zp9?M&#qFN|(|m2<OZwO1@#?i3<~fR|TAvxtA7*Qo?fHZz95d?WG5o5vO=2RqVmhs0`V^&N>Xi;nre5gehD55_+kKNdr)L2~aK$F0b%U8Dh8KIiits&u75&z0woX+Wo?v*VMhZu<wd2wb(LCw>$?qR%UXxOk4Y_DmPVm%r+eE#TMh6!emQnn{B<g0<r!dj1UVB1YdwLV-=OKn5AMWi!9!9fa$ufAqZJsGLovV#VixUbfXDxXqK27TxQ9_Vk>W1W;y0e)4rdw6Q&2w;XKR|exPgQ2_6xm4c5MqAq5SHePH@)p6aHlU0y(ADx5SPOp(VA#FS*G`sKy^W`5($C;DurU0(fC^h%1}xbw+;;z)(`*BWV~ax)ZK^NCA}r^x_{Qcub*yyZH`vnuuV*;L24J~OoiFFneyB*AID@p34+wli{%9LHh~@4Fu@)^~09<EKwYy#Go2B4tRA^_bzZJ{#gf-3uU7%f}FL27`e;(6ooZV)p?aq#Jva#gB3=*|A!wbP>?nHL#XVEvX>+5NH|}A^R3{BQ}pUhF`Q|F*`Y7gJYyW)^$pF$cbVeM{8~*mDv$<8ZoT>_JG?A7(_g&dOdQ&G1&ogJCehl<e`!rDtBS+h4`oiT+5G0e$bftz=ovvQ8?%S*1P}mJo~MCzl_4pS;_h>|D3~CD2BiE%^3|^!8jT;(U4x9#a*BN+2ZiJOTLd8e}dG|9#}+5k+I0CF>(hjYDWWM>3JH@gl<C$V?xG+u<y(4S<M%Lk(-Tq=apQ=BazVusJI{0qaLpNaxvf%pb`%CS}gy9N>^^NGvy`<k#U1Ti%rDwyEtBm<2jBd^GdNvR0WlFRSc<ok#->$M)7xE8o6}R6%2apOgIi&XXKcWCOc5*e`(0YppJ1Ph8%KO#QYEB2SYjMN)QsSxGn(G+y$OtkjH1uR2C+AP2&@3P}wtxnzD2tcoOw0F|fXSGz+9kPjecR`7Mcm-GS7u?b}2`$$a4HcdA0d6vP^PE$c$?y9!2|!&k|poehcx00i=0gs4Ojm=|wCZ%2|sz6aH!cp)u!!!g<mheYg#p*HTy)S=(G#ClCrtR;eO4~mCPLXZzHuxg)F-v25&HSJx~s&rZecF&_A#J+1(X(XBs>POIvWVuhBfMeTezr+qJx7>+`RxL-X<a4=4%QfiF6_6nmEf%U}L;Kn%ah0uBY880sZ~|`hfqZB&zkJ;A6S-c5;Abhd6_yNAvlx1fC|#m0DWWtuxy~!}2G@+eW1pvY)_MjFlKZ(901F8qija|-|6q%$U`1k0S0IT>i}$5s7Dw3f16w#|e74xaY)6>H4p`Xh2~}AxL@0~7+J5KRY7XafRJg=@s6%n$+5;7i|2qiilN!O?do-pEypa!(iy3kxl#N10jRFDBq-s``)Jzb<bTpF{w2_lmogF`s*Sp+;vh8iCA(ti0P)XUIVVYf-Cj+M0i4d8_q)b=HnfDg6Z5tOqjoOwulR>-Vr3hKPE3fF;HpDvil7;V4;f+qB<5#NjG@1!-qMbK~=Bz23bJ}KhlR~i5!3?@%Y&vFB>|PUdl$g7#JFkhkU9^ig#D+>tRk8Co#70VNB*lIRnQ1=|g_ryc$WN&~W3T<*u^(vh>uCRYkDn%=kFhNRO%%`%EdS|ZlwmbgQS7sE-HN02rdI)!1uXq^8O3tBlhy&`oA(t}wO4Gc(y)~^bBq4>@)XQr^yS29EyC}K8D5`Y6t5_vp4E25Hj4K#4mQ5Uio}cKhS}k!+~I^FwV$d8(l4M4GWuQ9@SN&*7>eW>&2aybwx@leMnLO^xBr@Wzk~N;uwzi{X^wofBVU)4Iq9ois1FAY>hv4$Wy`p(ExXiP?TJt))XAn`PoQ30Xue=bHBPlgJvoMRurhx>8Ef-dfZWQI+|`lwdbjjOtt5b8T{`+yGUzqTSg$R1N7Vvkr*|`4z_BSH`s_|F<hvaj9#b_^HHC8R7G8r%)7;&XvRduLN-lZe(LB6ilrYKg?e7i0;-54&c{>EdRtQQ5axZDz*1iV~1xe}+8aq7qZM@p8;P-Adc$0d9ChfR^wOk~n%DwCGZFk+ayAP^^yH!}|ug72_IwmN!V(!R6%5-!`c+~05b_}n>n&L%=;sY?+ePWMFB@K4=pBpql7BJ*CqrN#5M*Ub(r>_AM><Y4e<L2@LcYwU1(+9eB<gKG_UAk>l=<WXUs;hF<Rk@NXH*^xW!x}-}j^wSQ0I5qd@Rq-aneKt6d#I^|y}_wfwdBaCV=$c_))v+Mk-T?R0M{kW`E@uI6J^v*KfSM<CIhUDz64WanC2eCK(FW6hn*>S(ogkcc4{&G0_O{yuS#58iHnr3(97vz8R8P=Xm8fn;tt1WO_SZrlb&QgFYxr~`B|eJj41`DXk1*>Kh&$)aoy}pmF#R<lsUR)YV)3+o8;vi@u_V(u<26=92lZIL(VzkI2g*4Gux&08SP(VNJ6!FSmzLZHfpyojlhzIUZz~TvwFc)oay_R;JjX|PoBnhTbCk>ZMQ^!8QM|FlfqC{nSPrb{k)-%zp+@i7})55(!~ciOQGpc+wHM^#Gm!I@zA2hRT0XrS`**IeDwMT2;)7V`(dp0!48J>d)=hQoIc*3pwUr;?(?kV```C;Q~MwDeJuC""",
}
os.makedirs("g15_home", exist_ok=True)
for _n, _lit in _MODULES.items():
    with open(os.path.join("g15_home", _n), "w") as _fh:
        _fh.write(_text(_lit))

# =====================================================================
# GATE-15 KERNEL 1 — W-B2 COMPLETION (source / functionals / solve /
# shell sign), packaged under the 2026-11-23 standing order (heavy
# compute off the VM; parent launches on Kaggle, one at a time).
#
# Self-contained: all gate data and gate modules are embedded above
# (zlib/base85) and materialised into ./g15_home/ at start. The carried
# modules are Gate-15's OWN W-B2 code (written from scratch for this
# gate; NOT phase code), with exactly one adaptation: the home
# absolute path prefix replaced by the local g15_home/ path (counts
# asserted at build time and recorded in BUILD_INFO).
#
# CONTROL GATES FIRST (porting standard S5): Stage 0 recomputes the
# channel functionals and asserts (i) they match the home checkpoint,
# (ii) the A1 member cross-check reproduces the CORRECTED member
# control [Rt_,n]_0 = -0.0152185839536870246 (the phase-stored value,
# vindicated by W-B2's A1 diagnosis: Gate-15's W-A control worker had
# used a wrong A''' jet for the interior exp(2 Phi_2); the diagnosis
# is re-run and asserted in Stage 0), (iii) the A2 truncation anchors
# reproduce Phase 90/91's stored values within their registered bars.
# A failed control aborts loudly and voids everything after it.
#
# AMENDMENT (2026-11-23, repair of the v1 launch failure — NOT a bar
# move; no deciding read's bar is touched): v1 aborted at Stage 0 on
# the single check "A1 jump_R == 0" (|jump_R| < 1e-12), reading
# jump_R = +3.3617694518376954105565534120486498773929070783924e-9.
# Diagnosis (home, closed-form read, 50- and 80-digit): that value is
# digit-for-digit the HOME stored value (wb2_functionals.json) — the
# port is faithful and the environment is exonerated. [R~] = 0 is
# exact for the exact member (Gate-9 G9-2), but the member as stored
# carries beta_MK rounded to 7 significant figures (2.142611); with
# d[R~]/dbeta_MK = 0.012000000000 the stored residual is exactly the
# rounding propagation 0.012 x (beta_stored - beta*) with
# beta* = 2.14261071985254568... (jump_R(beta*) = 2.7e-50) inside the
# stored constant's rounding interval. Phase 90's record already
# documents this exact read: "[R~]_0 control residual +3.36e-9 (the
# rounded stored beta, k)", the Phase-90/91 control floor 3.4e-9.
# The 1e-12 bar sat ~3400x below the stored member's own floor, so
# the check could never pass on ANY faithful evaluation. The check
# is repaired to (i) agreement with the home stored control at the
# sibling A1 standard (rel < 1e-9) AND (ii) |jump_R| <= 1e-8, a bound
# derived from the evaluation's own error scale: full rounding
# excursion of the stored constants is 0.012 x 5e-7 = 6e-9 < 1e-8,
# and 1e-8 remains >5 orders below every deciding scale in this
# gate (dissolution bar 1e-5 per unit eps; jump_Rn = 1.5e-2). Full
# record: gate15/STATUS.md addendum of 2026-11-23.
#
# Stages (each writes its JSON to ./g15_out/ as it lands and prints a
# verdict line; PROGRESS.json is updated per stage):
#   0 controls (functionals + A1 + A3 diagnosis + A2 anchors)
#   1 primary source recomputation + home-checkpoint agreement +
#     entering-order fits + confrontation vs Phase-122 literals
#   2 second path (200-point Gauss-Legendre, float64) + 5% agreement
#   3 response matrices from W-B1's settled basis jets; ranks; solves
#     in the full space AND the correctly classified (e) sets
#     (ell=1: 10 full / 6 (e)-quotient; ell=2,3: 8 (e)); residuals and
#     amplitudes vs the registered bars (residual <= 1e-5 per unit
#     eps^entering; amplitudes <= 1e2); numpy float64 and mpmath
#     40-digit arithmetics as two solver paths
#   4 shell sign on both mouths, both solves, corrected interior
#     control (and W-A's erroneous control, for the record), tail
#     bound from the kernel's own ell=4 extraction
#   5 checker: wb2_results.json + wb2_check.json (every comparison)
#
# In-kernel judgements are PROVISIONAL until re-judged at home in a
# fresh process (porting standard S5). INTERNAL only.
# (V-b) UNDECIDED: Pais-Uhlenbeck spin-2 ghost vs Mannheim
# PT-symmetric quantisation — opposed literature positions, B3 NOT
# COMPUTABLE (Phase 32). Carried, not decided.
# =====================================================================
import json, os, subprocess, sys, time
from math import factorial

T0 = time.time()
HOME_DIR = os.path.join(os.getcwd(), "g15_home")
OUT_DIR = os.path.join(os.getcwd(), "g15_out")
os.makedirs(HOME_DIR, exist_ok=True)
os.makedirs(OUT_DIR, exist_ok=True)

def log(msg):
    print(f"[{time.time()-T0:8.1f}s] {msg}", flush=True)

def dump(name, obj):
    with open(os.path.join(OUT_DIR, name), "w") as fh:
        json.dump(obj, fh, indent=1)
    log(f"wrote g15_out/{name}")

def progress(stage, status):
    p = {"stage": stage, "status": status, "elapsed_s": time.time() - T0}
    with open(os.path.join(OUT_DIR, "PROGRESS.json"), "w") as fh:
        json.dump(p, fh, indent=1)
    log(f"STAGE {stage}: {status}")

def run_module(fname):
    log(f"running carried module {fname} ...")
    r = subprocess.run([sys.executable, os.path.join(HOME_DIR, fname)],
                       capture_output=True, text=True, cwd=os.getcwd())
    tail = "\n".join((r.stdout or "").splitlines()[-6:])
    log(f"{fname} stdout tail:\n{tail}")
    if r.returncode != 0:
        log(f"{fname} STDERR tail:\n" + "\n".join((r.stderr or "").splitlines()[-12:]))
        raise SystemExit(f"CONTROL GATE FAILED: carried module {fname} exited {r.returncode}")

def rel(a, b):
    a = float(a); b = float(b)
    return abs(a - b) / max(abs(b), 1e-300)

CHECKS = []
def check(name, ok, detail):
    CHECKS.append({"name": name, "pass": bool(ok), "detail": str(detail)})
    log(f"CHECK {'PASS' if ok else 'FAIL'}: {name} — {detail}")

# ---------------------------------------------------------------------
# STAGE 0 — controls
# ---------------------------------------------------------------------
progress(0, "running")
run_module("wb2_functionals.py")
func_new = json.load(open(os.path.join(HOME_DIR, "wb2_functionals.json")))
func_home = FUNC_HOME  # embedded home checkpoint (dict)
for key in ("LK_U_U1_V", "LR_U_U1_U2_V_V1", "LRn_U_U1_U2_U3_V_V1_V2"):
    worst = max(rel(x, y) for x, y in zip(func_new[key], func_home[key]))
    check(f"functionals {key} match home checkpoint", worst < 1e-9, f"max rel diff {worst:.3e}")
# A1 corrected control
JUMP_RN_CONTROL = -0.0152185839536870246
S00_CONTROL = 0.0202914452715827
jr = float(func_new["A1"]["jump_Rn"]); s00 = float(func_new["A1"]["S00_over_alpha0"])
check("A1 jump_Rn == corrected member control", rel(jr, JUMP_RN_CONTROL) < 1e-9,
      f"fresh {jr:.16f} vs control {JUMP_RN_CONTROL}")
check("A1 S00/a0 == corrected member control", rel(s00, S00_CONTROL) < 1e-9,
      f"fresh {s00:.16f} vs control {S00_CONTROL}")
# Amended 2026-11-23 (see header AMENDMENT): the original exact-zero
# check (|jump_R| < 1e-12) was miscalibrated against the stored
# member's documented 3.4e-9 control floor (rounded stored beta_MK).
# Repaired form: home-control agreement at the sibling A1 standard
# AND the floor-derived bound |jump_R| <= 1e-8.
jr_R = float(func_new["A1"]["jump_R"]); jr_R_home = float(func_home["A1"]["jump_R"])
check("A1 jump_R == home control, within stored-member floor",
      rel(jr_R, jr_R_home) < 1e-9 and abs(jr_R) <= 1e-8,
      f"jump_R {func_new['A1']['jump_R']} vs home stored {func_home['A1']['jump_R']} "
      f"(floor 3.4e-9: rounded stored beta_MK; amended bound 1e-8)")
# A3 diagnosis (documents + corrects the W-A control error)
run_module("wb2_a1_patch.py")
func_diag = json.load(open(os.path.join(HOME_DIR, "wb2_functionals.json")))
diag = func_diag["A1_diagnosis"]
check("A3 diagnosis: true-A3 jump == A1 control",
      rel(diag["jump_Rn_with_true_A3"], JUMP_RN_CONTROL) < 1e-9,
      f"{diag['jump_Rn_with_true_A3']}")
check("A3 diagnosis: W-A-A3 jump reproduces W-A's erroneous value",
      rel(diag["jump_Rn_with_WA_A3"], -0.01531714654192940335) < 1e-5,
      f"{diag['jump_Rn_with_WA_A3']} vs W-A stated -0.01531714654192940335 "
      "(W-A's +0.0204228620559 shell value was a W-A machinery error; corrected control stands)")
# A2 truncation anchors (registered bars: 5% / 5% / 5% / 1%)
a2 = func_new["A2_truncation"]
b0 = float(a2["ell0"]["0.1"]["B_per"]); b1 = float(a2["ell1"]["0.1"]["B_per"])
b2v = float(a2["ell2"]["0.1"]["B_per"]); b3 = float(a2["ell3"]["0.1"]["B_per"])
for nm, v in (("ell0", b0), ("ell1", b1), ("ell2", b2v), ("ell3", b3)):
    check(f"A2 [B] c {nm} within 5% of 4.302e-3", rel(v, 4.302e-3) < 0.05, f"{v:.10e}")
check("A2 D3 [K]1 within 5%", rel(float(a2["ell1"]["0.1"]["K_per"]), -4.270543e-6) < 0.05,
      a2["ell1"]["0.1"]["K_per"])
check("A2 D3 [Rtn]1 within 5%", rel(float(a2["ell1"]["0.1"]["Rn_per"]), 5.514561e-5) < 0.05,
      a2["ell1"]["0.1"]["Rn_per"])
check("A2 [Rt]3 within 5%", rel(float(a2["ell3"]["0.1"]["R_per"]), 8.570444e-3) < 0.05,
      a2["ell3"]["0.1"]["R_per"])
sid = func_new["S_identity"]
check("A2 S identity S0=-2,S1=0,S2=0,S3=-2 within 1%",
      abs(float(sid["S0"]) + 2) < 0.02 and abs(float(sid["S1"])) < 0.02
      and abs(float(sid["S2"])) < 0.02 and abs(float(sid["S3"]) + 2) < 0.02,
      json.dumps(sid))
if not all(c["pass"] for c in CHECKS):
    dump("wb2_check.json", {"stage0_controls": CHECKS, "verdict": "CONTROL GATE FAILED — all later stages void"})
    raise SystemExit("CONTROL GATE FAILED at Stage 0 — see g15_out/wb2_check.json")
progress(0, "complete — all controls pass")

# ---------------------------------------------------------------------
# STAGE 1 — primary source: recompute, home agreement, fits, confront
# ---------------------------------------------------------------------
progress(1, "running")
run_module("wb2_source.py")
src_new = json.load(open(os.path.join(HOME_DIR, "wb2_source.json")))
src_home = SRC_HOME
# resolve eps keys by float value (decimal-string forms vary with dps)
def by_eps(modes_rec):
    return {float(k): v for k, v in modes_rec.items()}
SRCN = {l: by_eps(rec) for l, rec in src_new["modes"].items()}
SRCH = {l: by_eps(rec) for l, rec in src_home["modes"].items()}
worst = 0.0; worst_at = None
for l, modes in SRCH.items():
    for eps, rec in modes.items():
        for ch, val in rec["channels"].items():
            nv = float(SRCN[l][eps]["channels"][ch])
            r = rel(nv, val) if abs(float(val)) > 1e-25 else abs(nv - float(val))
            if r > worst: worst, worst_at = r, (l, eps, ch)
check("primary source matches home checkpoint (all modes/eps/channels)",
      worst < 1e-6, f"max rel diff {worst:.3e} at {worst_at}")

from mpmath import mp, mpf
mp.dps = 40
EPSF = [0.1, 1 / 30, 0.01, 0.003, 0.001]
EPS_MPF = [mpf("0.1"), mpf(1) / 30, mpf("0.01"), mpf("0.003"), mpf("0.001")]
CHANS = ["B", "K", "Rt", "Rtn", "hth", "kth"]

def fit_channel(l, ch, table):
    """Model: v(eps) = c_main eps^(l+1) + c_tail eps^l (tail only l>=2).
    Exact 2-param (or 1-param) least squares in mpmath over the 5 rows.
    `table` maps float(eps) -> record (SRCN[str(l)])."""
    vs = [mpf(table[e]["channels"][ch]) for e in EPSF]
    if l >= 2:
        A = [[EPS_MPF[i] ** (l + 1), EPS_MPF[i] ** l] for i in range(5)]
        # normal equations 2x2
        s11 = sum(A[i][0] ** 2 for i in range(5)); s12 = sum(A[i][0] * A[i][1] for i in range(5))
        s22 = sum(A[i][1] ** 2 for i in range(5))
        t1 = sum(A[i][0] * vs[i] for i in range(5)); t2 = sum(A[i][1] * vs[i] for i in range(5))
        det = s11 * s22 - s12 ** 2
        cm = (t1 * s22 - t2 * s12) / det; ct = (s11 * t2 - s12 * t1) / det
        resid = max(abs(vs[i] - (cm * A[i][0] + ct * A[i][1])) for i in range(5))
        return cm, ct, resid
    else:
        s11 = sum(EPS_MPF[i] ** (2 * (l + 1)) for i in range(5))
        t1 = sum(EPS_MPF[i] ** (l + 1) * vs[i] for i in range(5))
        cm = t1 / s11
        resid = max(abs(vs[i] - cm * EPS_MPF[i] ** (l + 1)) for i in range(5))
        return cm, mpf(0), resid

fits = {}
for l in (1, 2, 3, 4):
    fits[str(l)] = {}
    for ch in CHANS:
        cm, ct, resid = fit_channel(l, ch, SRCN[str(l)])
        fits[str(l)][ch] = {"main_per_eps^(l+1)": str(cm), "tail_per_eps^l": str(ct),
                            "fit_max_resid": str(resid)}
dump("wb2_source_fits.json", fits)
log("entering-order fits: " + "; ".join(
    f"l{l} {ch} main={fits[str(l)][ch]['main_per_eps^(l+1)'][:14]} tail={fits[str(l)][ch]['tail_per_eps^l'][:14]}"
    for l in (1, 2, 3) for ch in ("B", "Rtn", "Rt")))
# Confrontation vs Phase-122 full-system literals (P122-3 dipole data + P122-1)
PHASE_SRC = {
    ("1", "B"): 6.014537e-3, ("1", "K"): -4.254506e-6, ("1", "Rtn"): 1.622818e-3,
    ("1", "Rt"): 1.552938e-3, ("2", "Rt"): -1.213920e-4,
}
for (l, ch), pv in PHASE_SRC.items():
    gv = float(fits[l][ch]["main_per_eps^(l+1)"])
    check(f"source {ch} l={l} main coeff vs Phase-122 literal {pv:+.6e}",
          rel(gv, pv) < 0.05, f"gate {gv:+.10e} (rel diff {rel(gv, pv):.3e}, bar 5%)")
b2tail = float(fits["2"]["B"]["tail_per_eps^l"])
check("source [B]2 tail coeff vs Phase-122 extracted -1.268835e-5",
      rel(b2tail, -1.268835e-5) < 0.05, f"gate {b2tail:+.10e}")
FLOOR = 3.4e-9
for l, ch in (("1", "Rt"), ("2", "Rt")):
    gv = abs(float(fits[l][ch]["main_per_eps^(l+1)"]))
    check(f"blindness: [Rt] l={l} decided nonzero in full system",
          gv >= 1e3 * FLOOR, f"|coeff| {gv:.6e} vs 1e3*floor {1e3*FLOOR:.1e} — (t,r) identity does NOT extend")
progress(1, "complete")

# ---------------------------------------------------------------------
# STAGE 2 — second path (GL-200 float64) + agreement
# ---------------------------------------------------------------------
progress(2, "running")
run_module("wb2_second.py")
sec = json.load(open(os.path.join(HOME_DIR, "wb2_second.json")))
sec_fits = {}
for l in (1, 2, 3, 4):
    sec_fits[str(l)] = {}
    for ch in CHANS:
        # float version of the same fit
        import numpy as np
        vs = np.array([float(sec["modes"][str(l)][e][ch]) for e in
                       ["0.1", "0.03333333333333333", "0.01", "0.003", "0.001"]])
        ep = np.array([0.1, 1 / 30, 0.01, 0.003, 0.001])
        if l >= 2:
            A = np.stack([ep ** (l + 1), ep ** l], axis=1)
            coef, *_ = np.linalg.lstsq(A, vs, rcond=None)
            sec_fits[str(l)][ch] = {"main": float(coef[0]), "tail": float(coef[1])}
        else:
            A = ep ** (l + 1)
            sec_fits[str(l)][ch] = {"main": float(np.sum(A * vs) / np.sum(A * A)), "tail": 0.0}
agree = {}
for l in ("1", "2", "3"):
    for ch in CHANS:
        gv = float(fits[l][ch]["main_per_eps^(l+1)"])
        sv = sec_fits[l][ch]["main"]
        agree[f"l{l}_{ch}"] = rel(sv, gv) if abs(gv) > 1e-12 else abs(sv - gv)
worst_agree = max(agree.values())
check("second path (GL-200) source agreement within 5% on deciding coefficients",
      worst_agree < 0.05, f"max rel diff {worst_agree:.3e}")
dump("wb2_second_fits.json", {"second_path_fits": sec_fits, "agreement_vs_primary": agree})
progress(2, "complete")

# ---------------------------------------------------------------------
# STAGE 3 — response matrices + solves (the deciding computation)
# ---------------------------------------------------------------------
progress(3, "running")
import numpy as np
LK = [mpf(x) for x in func_new["LK_U_U1_V"]]
LR = [mpf(x) for x in func_new["LR_U_U1_U2_V_V1"]]
LRn = [mpf(x) for x in func_new["LRn_U_U1_U2_U3_V_V1_V2"]]
Bm0 = mpf(func_new["background"]["Bm0"]); rS = mpf(1000)

def resp_vec(jet):
    U, U1, U2, U3 = (mpf(jet["U"]), mpf(jet["Uprime"]), mpf(jet["Upp"]), mpf(jet["Uppp"]))
    V, V1, V2 = mpf(jet["V"]), mpf(jet["Vprime"]), mpf(jet["Vpp"])
    Th, Th1 = mpf(jet["Theta"]), mpf(jet["Thetaprime"])
    return [V,
            LK[0] * U + LK[1] * U1 + LK[2] * V,
            LR[0] * U + LR[1] * U1 + LR[2] * U2 + LR[3] * V + LR[4] * V1,
            LRn[0] * U + LRn[1] * U1 + LRn[2] * U2 + LRn[3] * U3 + LRn[4] * V + LRn[5] * V1 + LRn[6] * V2,
            Th,
            Th1 / (2 * mp.sqrt(Bm0)) - V / (2 * rS * Bm0 ** mpf("1.5"))]

basis = BASIS_JETS["modes"]
SETS = {
    "ell1_full10": ("ell1", basis["ell1"]["gauge_basis_class_a"] + basis["ell1"]["e_basis"]),
    "ell1_e6": ("ell1", basis["ell1"]["e_basis"]),
    "ell2_e8": ("ell2", basis["ell2"]["e_basis"]),
    "ell3_e8": ("ell3", basis["ell3"]["e_basis"]),
}
solve_out = {}
for set_name, (ellkey, elems) in SETS.items():
    l = int(ellkey[3:])
    R = [[resp_vec(e["jet_at_Sigma"])[ch] for e in elems] for ch in range(6)]  # 6 x n mpmath
    Rf = np.array([[float(x) for x in row] for row in R])
    sv = np.linalg.svd(Rf, compute_uv=False)
    rank = int(np.sum(sv > 1e-8 * sv[0])) if sv[0] > 0 else 0
    entry = {"n_elems": len(elems), "rank": rank,
             "svals": [float(x) for x in sv], "solves": {}}
    for power, fitkey in (("main", "main_per_eps^(l+1)"), ("tail", "tail_per_eps^l")):
        if power == "tail" and l < 2:
            continue
        s = [mpf(fits[str(l)][ch][fitkey]) for ch in CHANS]
        # numpy path
        af, *_ = np.linalg.lstsq(Rf, np.array([float(x) for x in s]), rcond=None)
        resid_f = np.array([float(x) for x in s]) - Rf @ af
        # mpmath path: Moore-Penrose pseudoinverse (minimum-norm solve;
        # the residual is the unique projection residual even when the
        # system is underdetermined, e.g. 8 directions of rank 6)
        n = len(elems)
        try:
            a_mp = list(mp.pinv(mp.matrix(R)) * mp.matrix(s))
            resid_mp = [s[ch] - sum(R[ch][j] * a_mp[j] for j in range(n)) for ch in range(6)]
            amp_mp = max(abs(x) for x in a_mp)
        except Exception as exc:
            a_mp, resid_mp, amp_mp = None, None, None
            log(f"{set_name} {power}: mpmath solve failed: {exc}")
        entry["solves"][power] = {
            "source_vector": [str(x) for x in s],
            "numpy": {"amplitudes": [float(x) for x in af],
                      "max_abs_amplitude": float(np.max(np.abs(af))),
                      "residuals": [float(x) for x in resid_f],
                      "max_abs_residual": float(np.max(np.abs(resid_f)))},
            "mpmath": ({"amplitudes": [str(x) for x in a_mp],
                        "max_abs_amplitude": str(amp_mp),
                        "residuals": [str(x) for x in resid_mp],
                        "max_abs_residual": str(max(abs(x) for x in resid_mp))} if a_mp is not None else None),
        }
        log(f"{set_name} {power}: rank {rank}; numpy max|resid| "
            f"{entry['solves'][power]['numpy']['max_abs_residual']:.3e}, max|amp| "
            f"{entry['solves'][power]['numpy']['max_abs_amplitude']:.3e}")
    solve_out[set_name] = entry
    check(f"response rank {set_name} == 6 (full)", rank == 6, f"rank {rank}, svals {[f'{x:.2e}' for x in sv]}")
dump("wb2_solve.json", solve_out)
BAR_RESID, BAR_AMP = 1e-5, 1e2
for set_name in ("ell1_e6", "ell2_e8", "ell3_e8"):
    for power, sv_ in solve_out[set_name]["solves"].items():
        mr = sv_["numpy"]["max_abs_residual"]; ma = sv_["numpy"]["max_abs_amplitude"]
        check(f"CLOSE ({set_name}, {power}): residual <= 1e-5 and amplitudes <= 1e2",
              mr <= BAR_RESID and ma <= BAR_AMP, f"max|resid| {mr:.3e}, max|amp| {ma:.3e}")
for power, sv_ in solve_out["ell1_full10"]["solves"].items():
    mr = sv_["numpy"]["max_abs_residual"]
    log(f"ell1 full-10 {power} max|resid| {mr:.3e} (comparison record vs (e)-quotient)")
progress(3, "complete")

# ---------------------------------------------------------------------
# STAGE 4 — shell sign
# ---------------------------------------------------------------------
progress(4, "running")
def Ple(l, mu):
    if l == 0: return 1.0
    if l == 1: return mu
    if l == 2: return (3 * mu * mu - 1) / 2
    if l == 3: return (5 * mu ** 3 - 3 * mu) / 2

def rtn_resid(set_name, power):
    sv_ = solve_out[set_name]["solves"].get(power)
    return float(sv_["numpy"]["residuals"][3]) if sv_ else 0.0  # channel idx 3 = Rtn

EPS_ROWS = [0.1, 1 / 30, 0.01]
mus = [(-1.0 + 2.0 * i / 400) for i in range(401)]
# ell=4 tail bound from the kernel's own source extraction (raw values)
tail_bound = {e: 2.0 * abs(float(SRCN["4"][e]["channels"]["Rtn"])) for e in EPS_ROWS}
shell = {}
for label, jump0, setmap in (
    ("corrected_gate_control", JUMP_RN_CONTROL, {"1": "ell1_e6", "2": "ell2_e8", "3": "ell3_e8"}),
    ("corrected_gate_control_full10_L1", JUMP_RN_CONTROL, {"1": "ell1_full10", "2": "ell2_e8", "3": "ell3_e8"}),
    ("WA_erroneous_control_for_record", -0.01531714654192940335, {"1": "ell1_e6", "2": "ell2_e8", "3": "ell3_e8"}),
):
    shell[label] = {}
    for eps in EPS_ROWS:
        for mouth in ("A", "B"):
            vals = []
            for mu in mus:
                tot = jump0
                for l in (1, 2, 3):
                    sgn = 1.0 if (mouth == "A" or l % 2 == 0) else -1.0
                    tot += sgn * rtn_resid(setmap[str(l)], "main") * eps ** (l + 1) * Ple(l, mu)
                    if l >= 2:
                        tot += sgn * rtn_resid(setmap[str(l)], "tail") * eps ** l * Ple(l, mu)
                vals.append(-(4.0 / 3.0) * tot)
            mn = min(vals)
            shell[label][f"eps={eps}"] = shell[label].get(f"eps={eps}", {})
            shell[label][f"eps={eps}"][mouth] = {
                "min_S00_over_alpha0": mn,
                "min_minus_tail_bound": mn - (4.0 / 3.0) * tail_bound[eps],
                "tail_bound_on_Rtn": tail_bound[eps]}
    log(f"shell {label}: " + "; ".join(
        f"eps={e} A {shell[label][f'eps={e}']['A']['min_S00_over_alpha0']:.10f} "
        f"B {shell[label][f'eps={e}']['B']['min_S00_over_alpha0']:.10f}" for e in EPS_ROWS))
dump("wb2_shell.json", shell)
prim = shell["corrected_gate_control"]
for e in EPS_ROWS:
    for mouth in ("A", "B"):
        check(f"shell sign > 0 (corrected control, eps={e}, mouth {mouth})",
              prim[f"eps={e}"][mouth]["min_minus_tail_bound"] > 0,
              f"min {prim[f'eps={e}'][mouth]['min_S00_over_alpha0']:.10f}, "
              f"after tail bound {prim[f'eps={e}'][mouth]['min_minus_tail_bound']:.10f}")
mn01 = min(prim[f"eps={e}"][m]["min_S00_over_alpha0"] for e in EPS_ROWS for m in ("A", "B"))
check("shell minimum vs Phase-122 claimed +0.0202914453 (5% confrontation)",
      rel(mn01, 0.0202914453) < 0.05, f"gate min {mn01:.10f}")
log(f"tail bounds on [Rt_,n] by eps: {tail_bound} — Phase-122 stored-table bound 2.06e-6 at eps=0.1; "
    f"Phase-133 corrected total 2.459e-6 (gate's own ell=4 extraction gives {tail_bound[0.1]:.4e})")
progress(4, "complete")

# ---------------------------------------------------------------------
# STAGE 5 — checker assembly
# ---------------------------------------------------------------------
progress(5, "running")
results = {
    "kernel": "g15_wb2_kernel", "build_info": BUILD_INFO,
    "controls_stage0": "see wb2_check.json",
    "source_fits": fits, "second_path_fits": sec_fits,
    "second_path_agreement": agree, "solve": solve_out, "shell": shell,
    "tail_bound": {str(k): v for k, v in tail_bound.items()},
    "note": "In-kernel judgements provisional until re-judged at home in a fresh process.",
}
dump("wb2_results.json", results)
npass = sum(1 for c in CHECKS if c["pass"]); nfail = len(CHECKS) - npass
dump("wb2_check.json", {"checks": CHECKS, "n_pass": npass, "n_fail": nfail,
                        "verdict": f"{npass}/{len(CHECKS)} PASS"})
log(f"CHECKER: {npass}/{len(CHECKS)} PASS")
progress(5, "complete — kernel 1 finished")
print("G15_WB2_KERNEL_DONE", flush=True)
