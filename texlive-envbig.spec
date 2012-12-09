# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/envbig
# catalog-date 2008-11-11 20:51:43 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-envbig
Version:	20081111
Release:	2
Summary:	Printing addresses on envelopes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/envbig
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/envbig.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/envbig.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A simple package, that prints both 'from' and 'to' addresses.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20081111-2
+ Revision: 751488
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20081111-1
+ Revision: 718339
- texlive-envbig
- texlive-envbig
- texlive-envbig
- texlive-envbig

