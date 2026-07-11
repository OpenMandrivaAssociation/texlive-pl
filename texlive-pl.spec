%global tl_name pl
%global tl_revision 58661

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.09a
Release:	%{tl_revision}.1
Summary:	Polish extension of Computer Modern fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/polish/pl-mf.zip
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pl.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The Polish extension of the Computer Modern fonts (compatible with CM
itself) for use with Polish TeX formats. The fonts were originally a
part of the MeX distribution (and they are still available that way).

