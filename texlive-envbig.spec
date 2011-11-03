# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/envbig
# catalog-date 2008-11-11 20:51:43 +0100
# catalog-license lppl
# catalog-version undef
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
