%global d_conf                  %{_sysconfdir}/fonts
%global d_fonts                 %{_datadir}/fonts/fonts.custom.d

%global release_prefix          100

Name:                           ext-font
Version:                        1.0.3
Release:                        %{release_prefix}%{?dist}
Summary:                        META-package for install and configure fonts
License:                        MIT
Vendor:                         Package Store <https://pkgstore.github.io>
Packager:                       Kitsune Solar <kitsune.solar@gmail.com>

Source10:                       local.conf

Source100:                      FiraCode-Bold.ttf
Source101:                      FiraCode-Light.ttf
Source102:                      FiraCode-Medium.ttf
Source103:                      FiraCode-Regular.ttf
Source104:                      FiraCode-Retina.ttf
Source105:                      FiraCode-SemiBold.ttf

Source110:                      Candara.ttf
Source111:                      Candarab.ttf
Source112:                      Candarai.ttf
Source113:                      Candaral.ttf
Source114:                      Candarali.ttf
Source115:                      Candaraz.ttf
Source116:                      Gabriola.ttf
Source117:                      Inkfree.ttf
Source118:                      LeelUIsl.ttf
Source119:                      LeelaUIb.ttf
Source120:                      LeelawUI.ttf
Source121:                      Nirmala.ttf
Source122:                      NirmalaB.ttf
Source123:                      NirmalaS.ttf
Source124:                      arial.ttf
Source125:                      arialbd.ttf
Source126:                      arialbi.ttf
Source127:                      ariali.ttf
Source128:                      ariblk.ttf
Source129:                      bahnschrift.ttf
Source130:                      calibri.ttf
Source131:                      calibrib.ttf
Source132:                      calibrii.ttf
Source133:                      calibril.ttf
Source134:                      calibrili.ttf
Source135:                      calibriz.ttf
Source136:                      cambriab.ttf
Source137:                      cambriai.ttf
Source138:                      cambriaz.ttf
Source139:                      comic.ttf
Source140:                      comicbd.ttf
Source141:                      comici.ttf
Source142:                      comicz.ttf
Source143:                      consola.ttf
Source144:                      consolab.ttf
Source145:                      consolai.ttf
Source146:                      consolaz.ttf
Source147:                      constan.ttf
Source148:                      constanb.ttf
Source149:                      constani.ttf
Source150:                      constanz.ttf
Source151:                      corbel.ttf
Source152:                      corbelb.ttf
Source153:                      corbeli.ttf
Source154:                      corbell.ttf
Source155:                      corbelli.ttf
Source156:                      corbelz.ttf
Source157:                      cour.ttf
Source158:                      courbd.ttf
Source159:                      courbi.ttf
Source160:                      couri.ttf
Source161:                      ebrima.ttf
Source162:                      ebrimabd.ttf
Source163:                      framd.ttf
Source164:                      framdit.ttf
Source165:                      gadugi.ttf
Source166:                      gadugib.ttf
Source167:                      georgia.ttf
Source168:                      georgiab.ttf
Source169:                      georgiai.ttf
Source170:                      georgiaz.ttf
Source171:                      himalaya.ttf
Source172:                      holomdl2.ttf
Source173:                      impact.ttf
Source174:                      javatext.ttf
Source175:                      lucon.ttf
Source176:                      l_10646.ttf
Source177:                      malgun.ttf
Source178:                      malgunbd.ttf
Source179:                      malgunsl.ttf
Source180:                      marlett.ttf
Source181:                      micross.ttf
Source182:                      mmrtext.ttf
Source183:                      mmrtextb.ttf
Source184:                      monbaiti.ttf
Source185:                      msyi.ttf
Source186:                      mvboli.ttf
Source187:                      ntailu.ttf
Source188:                      ntailub.ttf
Source189:                      pala.ttf
Source190:                      palab.ttf
Source191:                      palabi.ttf
Source192:                      palai.ttf
Source193:                      phagspa.ttf
Source194:                      phagspab.ttf
Source195:                      segmdl2.ttf
Source196:                      segoepr.ttf
Source197:                      segoeprb.ttf
Source198:                      segoesc.ttf
Source199:                      segoescb.ttf
Source200:                      segoeui.ttf
Source201:                      segoeuib.ttf
Source202:                      segoeuii.ttf
Source203:                      segoeuil.ttf
Source204:                      segoeuisl.ttf
Source205:                      segoeuiz.ttf
Source206:                      seguibl.ttf
Source207:                      seguibli.ttf
Source208:                      seguiemj.ttf
Source209:                      seguihis.ttf
Source210:                      seguili.ttf
Source211:                      seguisb.ttf
Source212:                      seguisbi.ttf
Source213:                      seguisli.ttf
Source214:                      seguisym.ttf
Source215:                      simsunb.ttf
Source216:                      sylfaen.ttf
Source217:                      symbol.ttf
Source218:                      tahoma.ttf
Source219:                      tahomabd.ttf
Source220:                      taile.ttf
Source221:                      taileb.ttf
Source222:                      times.ttf
Source223:                      timesbd.ttf
Source224:                      timesbi.ttf
Source225:                      timesi.ttf
Source226:                      trebuc.ttf
Source227:                      trebucbd.ttf
Source228:                      trebucbi.ttf
Source229:                      trebucit.ttf
Source230:                      verdana.ttf
Source231:                      verdanab.ttf
Source232:                      verdanai.ttf
Source233:                      verdanaz.ttf
Source234:                      webdings.ttf
Source235:                      wingding.ttf

Requires:                       freetype
Requires:                       google-roboto-fonts google-roboto-condensed-fonts
Requires:                       google-noto-sans-fonts google-noto-serif-fonts
Requires:                       google-noto-emoji-fonts google-noto-emoji-color-fonts
Requires:                       google-noto-music-fonts google-noto-cjk-fonts
Requires:                       mozilla-fira-sans-fonts mozilla-fira-mono-fonts

%description
META-package for install and configure fonts.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%prep


%install
%{__rm} -rf %{buildroot}

%{__install} -dp -m 0755 %{buildroot}%{d_fonts}
%{__install} -dp -m 0755 %{buildroot}%{d_fonts}/fira-code
%{__install} -dp -m 0755 %{buildroot}%{d_fonts}/microsoft

%{__install} -Dp -m 0644 %{SOURCE10} \
  %{buildroot}%{d_conf}/local.conf

%{__install} -Dp -m 0644 %{SOURCE100} \
  %{buildroot}%{d_fonts}/fira-code/FiraCode-Bold.ttf
%{__install} -Dp -m 0644 %{SOURCE101} \
  %{buildroot}%{d_fonts}/fira-code/FiraCode-Light.ttf
%{__install} -Dp -m 0644 %{SOURCE102} \
  %{buildroot}%{d_fonts}/fira-code/FiraCode-Medium.ttf
%{__install} -Dp -m 0644 %{SOURCE103} \
  %{buildroot}%{d_fonts}/fira-code/FiraCode-Regular.ttf
%{__install} -Dp -m 0644 %{SOURCE104} \
  %{buildroot}%{d_fonts}/fira-code/FiraCode-Retina.ttf
%{__install} -Dp -m 0644 %{SOURCE105} \
  %{buildroot}%{d_fonts}/fira-code/FiraCode-SemiBold.ttf

%{__install} -Dp -m 0644 %{SOURCE110} \
  %{buildroot}%{d_fonts}/microsoft/Candara.ttf
%{__install} -Dp -m 0644 %{SOURCE111} \
  %{buildroot}%{d_fonts}/microsoft/Candarab.ttf
%{__install} -Dp -m 0644 %{SOURCE112} \
  %{buildroot}%{d_fonts}/microsoft/Candarai.ttf
%{__install} -Dp -m 0644 %{SOURCE113} \
  %{buildroot}%{d_fonts}/microsoft/Candaral.ttf
%{__install} -Dp -m 0644 %{SOURCE114} \
  %{buildroot}%{d_fonts}/microsoft/Candarali.ttf
%{__install} -Dp -m 0644 %{SOURCE115} \
  %{buildroot}%{d_fonts}/microsoft/Candaraz.ttf
%{__install} -Dp -m 0644 %{SOURCE116} \
  %{buildroot}%{d_fonts}/microsoft/Gabriola.ttf
%{__install} -Dp -m 0644 %{SOURCE117} \
  %{buildroot}%{d_fonts}/microsoft/Inkfree.ttf
%{__install} -Dp -m 0644 %{SOURCE118} \
  %{buildroot}%{d_fonts}/microsoft/LeelUIsl.ttf
%{__install} -Dp -m 0644 %{SOURCE119} \
  %{buildroot}%{d_fonts}/microsoft/LeelaUIb.ttf
%{__install} -Dp -m 0644 %{SOURCE120} \
  %{buildroot}%{d_fonts}/microsoft/LeelawUI.ttf
%{__install} -Dp -m 0644 %{SOURCE121} \
  %{buildroot}%{d_fonts}/microsoft/Nirmala.ttf
%{__install} -Dp -m 0644 %{SOURCE122} \
  %{buildroot}%{d_fonts}/microsoft/NirmalaB.ttf
%{__install} -Dp -m 0644 %{SOURCE123} \
  %{buildroot}%{d_fonts}/microsoft/NirmalaS.ttf
%{__install} -Dp -m 0644 %{SOURCE124} \
  %{buildroot}%{d_fonts}/microsoft/arial.ttf
%{__install} -Dp -m 0644 %{SOURCE125} \
  %{buildroot}%{d_fonts}/microsoft/arialbd.ttf
%{__install} -Dp -m 0644 %{SOURCE126} \
  %{buildroot}%{d_fonts}/microsoft/arialbi.ttf
%{__install} -Dp -m 0644 %{SOURCE127} \
  %{buildroot}%{d_fonts}/microsoft/ariali.ttf
%{__install} -Dp -m 0644 %{SOURCE128} \
  %{buildroot}%{d_fonts}/microsoft/ariblk.ttf
%{__install} -Dp -m 0644 %{SOURCE129} \
  %{buildroot}%{d_fonts}/microsoft/bahnschrift.ttf
%{__install} -Dp -m 0644 %{SOURCE130} \
  %{buildroot}%{d_fonts}/microsoft/calibri.ttf
%{__install} -Dp -m 0644 %{SOURCE131} \
  %{buildroot}%{d_fonts}/microsoft/calibrib.ttf
%{__install} -Dp -m 0644 %{SOURCE132} \
  %{buildroot}%{d_fonts}/microsoft/calibrii.ttf
%{__install} -Dp -m 0644 %{SOURCE133} \
  %{buildroot}%{d_fonts}/microsoft/calibril.ttf
%{__install} -Dp -m 0644 %{SOURCE134} \
  %{buildroot}%{d_fonts}/microsoft/calibrili.ttf
%{__install} -Dp -m 0644 %{SOURCE135} \
  %{buildroot}%{d_fonts}/microsoft/calibriz.ttf
%{__install} -Dp -m 0644 %{SOURCE136} \
  %{buildroot}%{d_fonts}/microsoft/cambriab.ttf
%{__install} -Dp -m 0644 %{SOURCE137} \
  %{buildroot}%{d_fonts}/microsoft/cambriai.ttf
%{__install} -Dp -m 0644 %{SOURCE138} \
  %{buildroot}%{d_fonts}/microsoft/cambriaz.ttf
%{__install} -Dp -m 0644 %{SOURCE139} \
  %{buildroot}%{d_fonts}/microsoft/comic.ttf
%{__install} -Dp -m 0644 %{SOURCE140} \
  %{buildroot}%{d_fonts}/microsoft/comicbd.ttf
%{__install} -Dp -m 0644 %{SOURCE141} \
  %{buildroot}%{d_fonts}/microsoft/comici.ttf
%{__install} -Dp -m 0644 %{SOURCE142} \
  %{buildroot}%{d_fonts}/microsoft/comicz.ttf
%{__install} -Dp -m 0644 %{SOURCE143} \
  %{buildroot}%{d_fonts}/microsoft/consola.ttf
%{__install} -Dp -m 0644 %{SOURCE144} \
  %{buildroot}%{d_fonts}/microsoft/consolab.ttf
%{__install} -Dp -m 0644 %{SOURCE145} \
  %{buildroot}%{d_fonts}/microsoft/consolai.ttf
%{__install} -Dp -m 0644 %{SOURCE146} \
  %{buildroot}%{d_fonts}/microsoft/consolaz.ttf
%{__install} -Dp -m 0644 %{SOURCE147} \
  %{buildroot}%{d_fonts}/microsoft/constan.ttf
%{__install} -Dp -m 0644 %{SOURCE148} \
  %{buildroot}%{d_fonts}/microsoft/constanb.ttf
%{__install} -Dp -m 0644 %{SOURCE149} \
  %{buildroot}%{d_fonts}/microsoft/constani.ttf
%{__install} -Dp -m 0644 %{SOURCE150} \
  %{buildroot}%{d_fonts}/microsoft/constanz.ttf
%{__install} -Dp -m 0644 %{SOURCE151} \
  %{buildroot}%{d_fonts}/microsoft/corbel.ttf
%{__install} -Dp -m 0644 %{SOURCE152} \
  %{buildroot}%{d_fonts}/microsoft/corbelb.ttf
%{__install} -Dp -m 0644 %{SOURCE153} \
  %{buildroot}%{d_fonts}/microsoft/corbeli.ttf
%{__install} -Dp -m 0644 %{SOURCE154} \
  %{buildroot}%{d_fonts}/microsoft/corbell.ttf
%{__install} -Dp -m 0644 %{SOURCE155} \
  %{buildroot}%{d_fonts}/microsoft/corbelli.ttf
%{__install} -Dp -m 0644 %{SOURCE156} \
  %{buildroot}%{d_fonts}/microsoft/corbelz.ttf
%{__install} -Dp -m 0644 %{SOURCE157} \
  %{buildroot}%{d_fonts}/microsoft/cour.ttf
%{__install} -Dp -m 0644 %{SOURCE158} \
  %{buildroot}%{d_fonts}/microsoft/courbd.ttf
%{__install} -Dp -m 0644 %{SOURCE159} \
  %{buildroot}%{d_fonts}/microsoft/courbi.ttf
%{__install} -Dp -m 0644 %{SOURCE160} \
  %{buildroot}%{d_fonts}/microsoft/couri.ttf
%{__install} -Dp -m 0644 %{SOURCE161} \
  %{buildroot}%{d_fonts}/microsoft/ebrima.ttf
%{__install} -Dp -m 0644 %{SOURCE162} \
  %{buildroot}%{d_fonts}/microsoft/ebrimabd.ttf
%{__install} -Dp -m 0644 %{SOURCE163} \
  %{buildroot}%{d_fonts}/microsoft/framd.ttf
%{__install} -Dp -m 0644 %{SOURCE164} \
  %{buildroot}%{d_fonts}/microsoft/framdit.ttf
%{__install} -Dp -m 0644 %{SOURCE165} \
  %{buildroot}%{d_fonts}/microsoft/gadugi.ttf
%{__install} -Dp -m 0644 %{SOURCE166} \
  %{buildroot}%{d_fonts}/microsoft/gadugib.ttf
%{__install} -Dp -m 0644 %{SOURCE167} \
  %{buildroot}%{d_fonts}/microsoft/georgia.ttf
%{__install} -Dp -m 0644 %{SOURCE168} \
  %{buildroot}%{d_fonts}/microsoft/georgiab.ttf
%{__install} -Dp -m 0644 %{SOURCE169} \
  %{buildroot}%{d_fonts}/microsoft/georgiai.ttf
%{__install} -Dp -m 0644 %{SOURCE170} \
  %{buildroot}%{d_fonts}/microsoft/georgiaz.ttf
%{__install} -Dp -m 0644 %{SOURCE171} \
  %{buildroot}%{d_fonts}/microsoft/himalaya.ttf
%{__install} -Dp -m 0644 %{SOURCE172} \
  %{buildroot}%{d_fonts}/microsoft/holomdl2.ttf
%{__install} -Dp -m 0644 %{SOURCE173} \
  %{buildroot}%{d_fonts}/microsoft/impact.ttf
%{__install} -Dp -m 0644 %{SOURCE174} \
  %{buildroot}%{d_fonts}/microsoft/javatext.ttf
%{__install} -Dp -m 0644 %{SOURCE175} \
  %{buildroot}%{d_fonts}/microsoft/lucon.ttf
%{__install} -Dp -m 0644 %{SOURCE176} \
  %{buildroot}%{d_fonts}/microsoft/l_10646.ttf
%{__install} -Dp -m 0644 %{SOURCE177} \
  %{buildroot}%{d_fonts}/microsoft/malgun.ttf
%{__install} -Dp -m 0644 %{SOURCE178} \
  %{buildroot}%{d_fonts}/microsoft/malgunbd.ttf
%{__install} -Dp -m 0644 %{SOURCE179} \
  %{buildroot}%{d_fonts}/microsoft/malgunsl.ttf
%{__install} -Dp -m 0644 %{SOURCE180} \
  %{buildroot}%{d_fonts}/microsoft/marlett.ttf
%{__install} -Dp -m 0644 %{SOURCE181} \
  %{buildroot}%{d_fonts}/microsoft/micross.ttf
%{__install} -Dp -m 0644 %{SOURCE182} \
  %{buildroot}%{d_fonts}/microsoft/mmrtext.ttf
%{__install} -Dp -m 0644 %{SOURCE183} \
  %{buildroot}%{d_fonts}/microsoft/mmrtextb.ttf
%{__install} -Dp -m 0644 %{SOURCE184} \
  %{buildroot}%{d_fonts}/microsoft/monbaiti.ttf
%{__install} -Dp -m 0644 %{SOURCE185} \
  %{buildroot}%{d_fonts}/microsoft/msyi.ttf
%{__install} -Dp -m 0644 %{SOURCE186} \
  %{buildroot}%{d_fonts}/microsoft/mvboli.ttf
%{__install} -Dp -m 0644 %{SOURCE187} \
  %{buildroot}%{d_fonts}/microsoft/ntailu.ttf
%{__install} -Dp -m 0644 %{SOURCE188} \
  %{buildroot}%{d_fonts}/microsoft/ntailub.ttf
%{__install} -Dp -m 0644 %{SOURCE189} \
  %{buildroot}%{d_fonts}/microsoft/pala.ttf
%{__install} -Dp -m 0644 %{SOURCE190} \
  %{buildroot}%{d_fonts}/microsoft/palab.ttf
%{__install} -Dp -m 0644 %{SOURCE191} \
  %{buildroot}%{d_fonts}/microsoft/palabi.ttf
%{__install} -Dp -m 0644 %{SOURCE192} \
  %{buildroot}%{d_fonts}/microsoft/palai.ttf
%{__install} -Dp -m 0644 %{SOURCE193} \
  %{buildroot}%{d_fonts}/microsoft/phagspa.ttf
%{__install} -Dp -m 0644 %{SOURCE194} \
  %{buildroot}%{d_fonts}/microsoft/phagspab.ttf
%{__install} -Dp -m 0644 %{SOURCE195} \
  %{buildroot}%{d_fonts}/microsoft/segmdl2.ttf
%{__install} -Dp -m 0644 %{SOURCE196} \
  %{buildroot}%{d_fonts}/microsoft/segoepr.ttf
%{__install} -Dp -m 0644 %{SOURCE197} \
  %{buildroot}%{d_fonts}/microsoft/segoeprb.ttf
%{__install} -Dp -m 0644 %{SOURCE198} \
  %{buildroot}%{d_fonts}/microsoft/segoesc.ttf
%{__install} -Dp -m 0644 %{SOURCE199} \
  %{buildroot}%{d_fonts}/microsoft/segoescb.ttf
%{__install} -Dp -m 0644 %{SOURCE200} \
  %{buildroot}%{d_fonts}/microsoft/segoeui.ttf
%{__install} -Dp -m 0644 %{SOURCE201} \
  %{buildroot}%{d_fonts}/microsoft/segoeuib.ttf
%{__install} -Dp -m 0644 %{SOURCE202} \
  %{buildroot}%{d_fonts}/microsoft/segoeuii.ttf
%{__install} -Dp -m 0644 %{SOURCE203} \
  %{buildroot}%{d_fonts}/microsoft/segoeuil.ttf
%{__install} -Dp -m 0644 %{SOURCE204} \
  %{buildroot}%{d_fonts}/microsoft/segoeuisl.ttf
%{__install} -Dp -m 0644 %{SOURCE205} \
  %{buildroot}%{d_fonts}/microsoft/segoeuiz.ttf
%{__install} -Dp -m 0644 %{SOURCE206} \
  %{buildroot}%{d_fonts}/microsoft/seguibl.ttf
%{__install} -Dp -m 0644 %{SOURCE207} \
  %{buildroot}%{d_fonts}/microsoft/seguibli.ttf
%{__install} -Dp -m 0644 %{SOURCE208} \
  %{buildroot}%{d_fonts}/microsoft/seguiemj.ttf
%{__install} -Dp -m 0644 %{SOURCE209} \
  %{buildroot}%{d_fonts}/microsoft/seguihis.ttf
%{__install} -Dp -m 0644 %{SOURCE210} \
  %{buildroot}%{d_fonts}/microsoft/seguili.ttf
%{__install} -Dp -m 0644 %{SOURCE211} \
  %{buildroot}%{d_fonts}/microsoft/seguisb.ttf
%{__install} -Dp -m 0644 %{SOURCE212} \
  %{buildroot}%{d_fonts}/microsoft/seguisbi.ttf
%{__install} -Dp -m 0644 %{SOURCE213} \
  %{buildroot}%{d_fonts}/microsoft/seguisli.ttf
%{__install} -Dp -m 0644 %{SOURCE214} \
  %{buildroot}%{d_fonts}/microsoft/seguisym.ttf
%{__install} -Dp -m 0644 %{SOURCE215} \
  %{buildroot}%{d_fonts}/microsoft/simsunb.ttf
%{__install} -Dp -m 0644 %{SOURCE216} \
  %{buildroot}%{d_fonts}/microsoft/sylfaen.ttf
%{__install} -Dp -m 0644 %{SOURCE217} \
  %{buildroot}%{d_fonts}/microsoft/symbol.ttf
%{__install} -Dp -m 0644 %{SOURCE218} \
  %{buildroot}%{d_fonts}/microsoft/tahoma.ttf
%{__install} -Dp -m 0644 %{SOURCE219} \
  %{buildroot}%{d_fonts}/microsoft/tahomabd.ttf
%{__install} -Dp -m 0644 %{SOURCE220} \
  %{buildroot}%{d_fonts}/microsoft/taile.ttf
%{__install} -Dp -m 0644 %{SOURCE221} \
  %{buildroot}%{d_fonts}/microsoft/taileb.ttf
%{__install} -Dp -m 0644 %{SOURCE222} \
  %{buildroot}%{d_fonts}/microsoft/times.ttf
%{__install} -Dp -m 0644 %{SOURCE223} \
  %{buildroot}%{d_fonts}/microsoft/timesbd.ttf
%{__install} -Dp -m 0644 %{SOURCE224} \
  %{buildroot}%{d_fonts}/microsoft/timesbi.ttf
%{__install} -Dp -m 0644 %{SOURCE225} \
  %{buildroot}%{d_fonts}/microsoft/timesi.ttf
%{__install} -Dp -m 0644 %{SOURCE226} \
  %{buildroot}%{d_fonts}/microsoft/trebuc.ttf
%{__install} -Dp -m 0644 %{SOURCE227} \
  %{buildroot}%{d_fonts}/microsoft/trebucbd.ttf
%{__install} -Dp -m 0644 %{SOURCE228} \
  %{buildroot}%{d_fonts}/microsoft/trebucbi.ttf
%{__install} -Dp -m 0644 %{SOURCE229} \
  %{buildroot}%{d_fonts}/microsoft/trebucit.ttf
%{__install} -Dp -m 0644 %{SOURCE230} \
  %{buildroot}%{d_fonts}/microsoft/verdana.ttf
%{__install} -Dp -m 0644 %{SOURCE231} \
  %{buildroot}%{d_fonts}/microsoft/verdanab.ttf
%{__install} -Dp -m 0644 %{SOURCE232} \
  %{buildroot}%{d_fonts}/microsoft/verdanai.ttf
%{__install} -Dp -m 0644 %{SOURCE233} \
  %{buildroot}%{d_fonts}/microsoft/verdanaz.ttf
%{__install} -Dp -m 0644 %{SOURCE234} \
  %{buildroot}%{d_fonts}/microsoft/webdings.ttf
%{__install} -Dp -m 0644 %{SOURCE235} \
  %{buildroot}%{d_fonts}/microsoft/wingding.ttf


%files
%dir %{d_fonts}
%dir %{d_fonts}/fira-code
%dir %{d_fonts}/microsoft
%config %{d_conf}/local.conf

%{d_fonts}/fira-code/FiraCode-Bold.ttf
%{d_fonts}/fira-code/FiraCode-Light.ttf
%{d_fonts}/fira-code/FiraCode-Medium.ttf
%{d_fonts}/fira-code/FiraCode-Regular.ttf
%{d_fonts}/fira-code/FiraCode-Retina.ttf
%{d_fonts}/fira-code/FiraCode-SemiBold.ttf

%{d_fonts}/microsoft/Candara.ttf
%{d_fonts}/microsoft/Candarab.ttf
%{d_fonts}/microsoft/Candarai.ttf
%{d_fonts}/microsoft/Candaral.ttf
%{d_fonts}/microsoft/Candarali.ttf
%{d_fonts}/microsoft/Candaraz.ttf
%{d_fonts}/microsoft/Gabriola.ttf
%{d_fonts}/microsoft/Inkfree.ttf
%{d_fonts}/microsoft/LeelUIsl.ttf
%{d_fonts}/microsoft/LeelaUIb.ttf
%{d_fonts}/microsoft/LeelawUI.ttf
%{d_fonts}/microsoft/Nirmala.ttf
%{d_fonts}/microsoft/NirmalaB.ttf
%{d_fonts}/microsoft/NirmalaS.ttf
%{d_fonts}/microsoft/arial.ttf
%{d_fonts}/microsoft/arialbd.ttf
%{d_fonts}/microsoft/arialbi.ttf
%{d_fonts}/microsoft/ariali.ttf
%{d_fonts}/microsoft/ariblk.ttf
%{d_fonts}/microsoft/bahnschrift.ttf
%{d_fonts}/microsoft/calibri.ttf
%{d_fonts}/microsoft/calibrib.ttf
%{d_fonts}/microsoft/calibrii.ttf
%{d_fonts}/microsoft/calibril.ttf
%{d_fonts}/microsoft/calibrili.ttf
%{d_fonts}/microsoft/calibriz.ttf
%{d_fonts}/microsoft/cambriab.ttf
%{d_fonts}/microsoft/cambriai.ttf
%{d_fonts}/microsoft/cambriaz.ttf
%{d_fonts}/microsoft/comic.ttf
%{d_fonts}/microsoft/comicbd.ttf
%{d_fonts}/microsoft/comici.ttf
%{d_fonts}/microsoft/comicz.ttf
%{d_fonts}/microsoft/consola.ttf
%{d_fonts}/microsoft/consolab.ttf
%{d_fonts}/microsoft/consolai.ttf
%{d_fonts}/microsoft/consolaz.ttf
%{d_fonts}/microsoft/constan.ttf
%{d_fonts}/microsoft/constanb.ttf
%{d_fonts}/microsoft/constani.ttf
%{d_fonts}/microsoft/constanz.ttf
%{d_fonts}/microsoft/corbel.ttf
%{d_fonts}/microsoft/corbelb.ttf
%{d_fonts}/microsoft/corbeli.ttf
%{d_fonts}/microsoft/corbell.ttf
%{d_fonts}/microsoft/corbelli.ttf
%{d_fonts}/microsoft/corbelz.ttf
%{d_fonts}/microsoft/cour.ttf
%{d_fonts}/microsoft/courbd.ttf
%{d_fonts}/microsoft/courbi.ttf
%{d_fonts}/microsoft/couri.ttf
%{d_fonts}/microsoft/ebrima.ttf
%{d_fonts}/microsoft/ebrimabd.ttf
%{d_fonts}/microsoft/framd.ttf
%{d_fonts}/microsoft/framdit.ttf
%{d_fonts}/microsoft/gadugi.ttf
%{d_fonts}/microsoft/gadugib.ttf
%{d_fonts}/microsoft/georgia.ttf
%{d_fonts}/microsoft/georgiab.ttf
%{d_fonts}/microsoft/georgiai.ttf
%{d_fonts}/microsoft/georgiaz.ttf
%{d_fonts}/microsoft/himalaya.ttf
%{d_fonts}/microsoft/holomdl2.ttf
%{d_fonts}/microsoft/impact.ttf
%{d_fonts}/microsoft/javatext.ttf
%{d_fonts}/microsoft/lucon.ttf
%{d_fonts}/microsoft/l_10646.ttf
%{d_fonts}/microsoft/malgun.ttf
%{d_fonts}/microsoft/malgunbd.ttf
%{d_fonts}/microsoft/malgunsl.ttf
%{d_fonts}/microsoft/marlett.ttf
%{d_fonts}/microsoft/micross.ttf
%{d_fonts}/microsoft/mmrtext.ttf
%{d_fonts}/microsoft/mmrtextb.ttf
%{d_fonts}/microsoft/monbaiti.ttf
%{d_fonts}/microsoft/msyi.ttf
%{d_fonts}/microsoft/mvboli.ttf
%{d_fonts}/microsoft/ntailu.ttf
%{d_fonts}/microsoft/ntailub.ttf
%{d_fonts}/microsoft/pala.ttf
%{d_fonts}/microsoft/palab.ttf
%{d_fonts}/microsoft/palabi.ttf
%{d_fonts}/microsoft/palai.ttf
%{d_fonts}/microsoft/phagspa.ttf
%{d_fonts}/microsoft/phagspab.ttf
%{d_fonts}/microsoft/segmdl2.ttf
%{d_fonts}/microsoft/segoepr.ttf
%{d_fonts}/microsoft/segoeprb.ttf
%{d_fonts}/microsoft/segoesc.ttf
%{d_fonts}/microsoft/segoescb.ttf
%{d_fonts}/microsoft/segoeui.ttf
%{d_fonts}/microsoft/segoeuib.ttf
%{d_fonts}/microsoft/segoeuii.ttf
%{d_fonts}/microsoft/segoeuil.ttf
%{d_fonts}/microsoft/segoeuisl.ttf
%{d_fonts}/microsoft/segoeuiz.ttf
%{d_fonts}/microsoft/seguibl.ttf
%{d_fonts}/microsoft/seguibli.ttf
%{d_fonts}/microsoft/seguiemj.ttf
%{d_fonts}/microsoft/seguihis.ttf
%{d_fonts}/microsoft/seguili.ttf
%{d_fonts}/microsoft/seguisb.ttf
%{d_fonts}/microsoft/seguisbi.ttf
%{d_fonts}/microsoft/seguisli.ttf
%{d_fonts}/microsoft/seguisym.ttf
%{d_fonts}/microsoft/simsunb.ttf
%{d_fonts}/microsoft/sylfaen.ttf
%{d_fonts}/microsoft/symbol.ttf
%{d_fonts}/microsoft/tahoma.ttf
%{d_fonts}/microsoft/tahomabd.ttf
%{d_fonts}/microsoft/taile.ttf
%{d_fonts}/microsoft/taileb.ttf
%{d_fonts}/microsoft/times.ttf
%{d_fonts}/microsoft/timesbd.ttf
%{d_fonts}/microsoft/timesbi.ttf
%{d_fonts}/microsoft/timesi.ttf
%{d_fonts}/microsoft/trebuc.ttf
%{d_fonts}/microsoft/trebucbd.ttf
%{d_fonts}/microsoft/trebucbi.ttf
%{d_fonts}/microsoft/trebucit.ttf
%{d_fonts}/microsoft/verdana.ttf
%{d_fonts}/microsoft/verdanab.ttf
%{d_fonts}/microsoft/verdanai.ttf
%{d_fonts}/microsoft/verdanaz.ttf
%{d_fonts}/microsoft/webdings.ttf
%{d_fonts}/microsoft/wingding.ttf


%changelog
* Sun Jun 20 2021 Package Store <kitsune.solar@gmail.com> - 1.0.3-100
- UPD: "local.conf" - Add "Noto Emoji Color".

* Fri Jun 18 2021 Package Store <kitsune.solar@gmail.com> - 1.0.2-101
- UPD: New build for latest changes.

* Thu Jun 17 2021 Package Store <kitsune.solar@gmail.com> - 1.0.2-100
- UPD: Move to GitHub.
- UPD: License.

* Thu Jun 25 2020 Package Store <kitsune.solar@gmail.com> - 1.0.1-100
- ADD: MS Fonts and Fira Code.

* Sun Jul 28 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-101
- UPD: SPEC-file.

* Sat Jul 27 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-100
- Initial build.
