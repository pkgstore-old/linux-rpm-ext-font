%global d_conf                  %{_sysconfdir}/fonts
%global d_fonts                 %{_datadir}/fonts/fonts.custom.d

%global release_prefix          1000

Name:                           ext-font
Version:                        1.0.4
Release:                        %{release_prefix}%{?dist}
Summary:                        META-package for install and configure fonts
License:                        MIT

Source0:                        %{name}-%{version}.tar.xz

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

%{__install} -Dp -m 0644 fira-code-fonts/*.ttf \
  %{buildroot}%{d_fonts}/fira-code/
%{__install} -Dp -m 0644 microsoft-fonts/*.ttf \
  %{buildroot}%{d_fonts}/microsoft/
%{__install} -Dp -m 0644 local.conf \
  %{buildroot}%{d_conf}/local.conf


%files
%dir %{d_fonts}
%dir %{d_fonts}/fira-code
%dir %{d_fonts}/microsoft
%config %{d_conf}/local.conf

%{d_fonts}/fira-code/
%{d_fonts}/microsoft/


%changelog
* Sun Jun 20 2021 Package Store <pkgstore@mail.ru> - 1.0.4-1000
- UPD: Rebuild by Package Store.
- UPD: File "ext-font.spec".

* Sun Jun 20 2021 Package Store <pkgstore@mail.ru> - 1.0.3-100
- UPD: "local.conf" - Add "Noto Emoji Color".

* Fri Jun 18 2021 Package Store <pkgstore@mail.ru> - 1.0.2-101
- UPD: New build for latest changes.

* Thu Jun 17 2021 Package Store <pkgstore@mail.ru> - 1.0.2-100
- UPD: Move to GitHub.
- UPD: License.

* Thu Jun 25 2020 Package Store <pkgstore@mail.ru> - 1.0.1-100
- ADD: MS Fonts and Fira Code.

* Sun Jul 28 2019 Package Store <pkgstore@mail.ru> - 1.0.0-101
- UPD: SPEC-file.

* Sat Jul 27 2019 Package Store <pkgstore@mail.ru> - 1.0.0-100
- Initial build.
