%global tl_name envbig
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Printing addresses on envelopes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/envbig
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/envbig.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/envbig.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A simple package, that prints both 'from' and 'to' addresses.

