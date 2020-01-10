Name: hyphen-grc
Summary: Ancient Greek hyphenation rules
%define upstreamid 20110913
Version: 0.%{upstreamid}
Release: 4%{?dist}
#? in a url causes trouble
#http://tug.org/svn/texhyphen/trunk/hyph-utf8/tex/generic/hyph-utf8/patterns/tex/hyph-grc.tex?view=co
Source: hyph-grc.tex
Group: Applications/Text
URL: http://tug.org/tex-hyphen
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LPPL
BuildArch: noarch
BuildRequires: hyphen-devel
Requires: hyphen
Patch0: hyphen-grc-cleantex.patch

%description
Ancient Greek hyphenation rules.

%prep
%setup -T -q -c -n hyphen-grc
cp -p %{SOURCE0} hyph-grc.tex
%patch0 -p0 -b .clean

%build
grep -v "^%" hyph-grc.tex | tr ' ' '\n' > temp.tex
substrings.pl temp.tex temp.dic UTF-8
LANG=el_GR.utf8 uniq temp.dic > hyph_grc_GR.dic
echo "created with substring.pl by substrings.pl hyph-grc.tex hyph_grc_GR.dic UTF-8" > README
echo "---" >> README
head -n 37 hyph-grc.tex >> README

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_grc_GR.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%{_datadir}/hyphen/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20110913-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20110913-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20110913-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Caolán McNamara <caolanm@redhat.com> - 0.20110913-1
- latest version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20100531-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 01 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100531-1
- latest version

* Wed Oct 14 2009 Caolán McNamara <caolanm@redhat.com> - 0.20080616-1
- initial version
