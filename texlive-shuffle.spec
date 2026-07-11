%global tl_name shuffle
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	A symbol for the shuffle product
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/shuffle
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/shuffle.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/shuffle.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/shuffle.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides a LaTeX package and a font (as Metafont source) for
the shuffle product which is used in some part of mathematics and
physics.

