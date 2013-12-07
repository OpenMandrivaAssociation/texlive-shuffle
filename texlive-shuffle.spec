# revision 15878
# category Package
# catalog-ctan /fonts/shuffle
# catalog-date 2008-10-30 09:46:08 +0100
# catalog-license pd
# catalog-version 1.0
Name:		texlive-shuffle
Version:	1.0
Release:	4
Summary:	A symbol for the shuffle product
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/shuffle
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shuffle.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shuffle.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shuffle.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 755988
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719531
- texlive-shuffle
- texlive-shuffle
- texlive-shuffle
- texlive-shuffle

