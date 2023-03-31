Name:		texlive-tex-locale
Version:	48500
Release:	2
Summary:	Localisation support for TeX and LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tex-locale
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-locale.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-locale.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-locale.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package uses both tracklang and texosquery to look up the
locale information from the operating system and provide
commands that can access locale-dependent information, such as
the currency symbol and decimal separator. The file
tex-locale.tex provides generic TeX code. The LaTeX package
tex-locale.sty can additionally load babel or polyglossia with
the locale's language setting, as well as various other
packages such as fontspec (XeLaTeX/LuaLaTeX) or fontenc +
inputenc (pdfLaTeX).

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/tex-locale
%{_texmfdistdir}/tex/latex/tex-locale
%{_texmfdistdir}/tex/generic/tex-locale
%doc %{_texmfdistdir}/doc/generic/tex-locale

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
