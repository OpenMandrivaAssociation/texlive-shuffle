Name:		texlive-shuffle
Version:	15878
Release:	2
Summary:	A symbol for the shuffle product
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/shuffle
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shuffle.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shuffle.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shuffle.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides a LaTeX package and a font (as MetaFont
source) for the shuffle product which is used in some part of
mathematics and physics.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/shuffle/shuffle.mf
%{_texmfdistdir}/fonts/source/public/shuffle/shuffle10.mf
%{_texmfdistdir}/fonts/source/public/shuffle/shuffle7.mf
%{_texmfdistdir}/fonts/tfm/public/shuffle/shuffle10.tfm
%{_texmfdistdir}/fonts/tfm/public/shuffle/shuffle7.tfm
%{_texmfdistdir}/tex/latex/shuffle/Ushuffle.fd
%{_texmfdistdir}/tex/latex/shuffle/shuffle.sty
%doc %{_texmfdistdir}/doc/latex/shuffle/README
%doc %{_texmfdistdir}/doc/latex/shuffle/shuffle.pdf
#- source
%doc %{_texmfdistdir}/source/latex/shuffle/shuffle.dtx
%doc %{_texmfdistdir}/source/latex/shuffle/shuffle.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
