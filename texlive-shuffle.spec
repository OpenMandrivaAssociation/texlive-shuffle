# revision 15878
# category Package
# catalog-ctan /fonts/shuffle
# catalog-date 2008-10-30 09:46:08 +0100
# catalog-license pd
# catalog-version 1.0
Name:		texlive-shuffle
Version:	1.0
Release:	1
Summary:	A symbol for the shuffle product
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/shuffle
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shuffle.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shuffle.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shuffle.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The bundle provides a LaTeX package and a font (as MetaFont
source) for the shuffle product which is used in some part of
mathematics and physics.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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