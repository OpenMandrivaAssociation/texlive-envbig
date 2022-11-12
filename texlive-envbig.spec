Name:		texlive-envbig
Version:	15878
Release:	1
Summary:	Printing addresses on envelopes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/envbig
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/envbig.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/envbig.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
