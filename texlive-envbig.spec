Name:		texlive-envbig
Version:	20081111
Release:	1
Summary:	Printing addresses on envelopes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/envbig
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/envbig.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/envbig.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
A simple package, that prints both 'from' and 'to' addresses.

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
%{_texmfdistdir}/tex/latex/envbig/envbig.sty
%doc %{_texmfdistdir}/doc/latex/envbig/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
