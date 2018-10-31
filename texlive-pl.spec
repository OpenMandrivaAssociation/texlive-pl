# revision 15878
# category Package
# catalog-ctan /language/polish/plpsfont
# catalog-date 2009-10-07 21:35:42 +0200
# catalog-license pd
# catalog-version 1.15
Name:		texlive-pl
Version:	3.0
Release:	2
Summary:	Polish extension of CM fonts in Type 1 format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/polish/plpsfont
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pl.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex

%description
This package is the Polish extension of the Computer Modern
fonts (known as PL fonts),in Adobe Type 1 (PostScript) format.
The fonts use the same .tfm files as for the version generated
by MetaFont. This release of fonts was adapted to the (mostly
guessed) demands of the Windows environment, while keeping the
fonts usable with TeX; however, encoding files are now added,
as Windows and TeX use different encoding schemes.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pl/config.pl
%{_texmfdistdir}/fonts/afm/public/pl/plb10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plbsy10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plbx10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plbx12.afm
%{_texmfdistdir}/fonts/afm/public/pl/plbx5.afm
%{_texmfdistdir}/fonts/afm/public/pl/plbx6.afm
%{_texmfdistdir}/fonts/afm/public/pl/plbx7.afm
%{_texmfdistdir}/fonts/afm/public/pl/plbx8.afm
%{_texmfdistdir}/fonts/afm/public/pl/plbx9.afm
%{_texmfdistdir}/fonts/afm/public/pl/plbxsl10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plbxti10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plcsc10.afm
%{_texmfdistdir}/fonts/afm/public/pl/pldunh10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plex10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plex9.afm
%{_texmfdistdir}/fonts/afm/public/pl/plff10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plfi10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plfib8.afm
%{_texmfdistdir}/fonts/afm/public/pl/plinch.afm
%{_texmfdistdir}/fonts/afm/public/pl/plitt10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plmi10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plmi12.afm
%{_texmfdistdir}/fonts/afm/public/pl/plmi5.afm
%{_texmfdistdir}/fonts/afm/public/pl/plmi6.afm
%{_texmfdistdir}/fonts/afm/public/pl/plmi7.afm
%{_texmfdistdir}/fonts/afm/public/pl/plmi8.afm
%{_texmfdistdir}/fonts/afm/public/pl/plmi9.afm
%{_texmfdistdir}/fonts/afm/public/pl/plmib10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plr10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plr12.afm
%{_texmfdistdir}/fonts/afm/public/pl/plr17.afm
%{_texmfdistdir}/fonts/afm/public/pl/plr5.afm
%{_texmfdistdir}/fonts/afm/public/pl/plr6.afm
%{_texmfdistdir}/fonts/afm/public/pl/plr7.afm
%{_texmfdistdir}/fonts/afm/public/pl/plr8.afm
%{_texmfdistdir}/fonts/afm/public/pl/plr9.afm
%{_texmfdistdir}/fonts/afm/public/pl/plsl10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plsl12.afm
%{_texmfdistdir}/fonts/afm/public/pl/plsl8.afm
%{_texmfdistdir}/fonts/afm/public/pl/plsl9.afm
%{_texmfdistdir}/fonts/afm/public/pl/plsltt10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plss10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plss12.afm
%{_texmfdistdir}/fonts/afm/public/pl/plss17.afm
%{_texmfdistdir}/fonts/afm/public/pl/plss8.afm
%{_texmfdistdir}/fonts/afm/public/pl/plss9.afm
%{_texmfdistdir}/fonts/afm/public/pl/plssbi10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plssbx10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plssdc10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plssi10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plssi12.afm
%{_texmfdistdir}/fonts/afm/public/pl/plssi17.afm
%{_texmfdistdir}/fonts/afm/public/pl/plssi8.afm
%{_texmfdistdir}/fonts/afm/public/pl/plssi9.afm
%{_texmfdistdir}/fonts/afm/public/pl/plssq8.afm
%{_texmfdistdir}/fonts/afm/public/pl/plssqi8.afm
%{_texmfdistdir}/fonts/afm/public/pl/plsy10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plsy5.afm
%{_texmfdistdir}/fonts/afm/public/pl/plsy6.afm
%{_texmfdistdir}/fonts/afm/public/pl/plsy7.afm
%{_texmfdistdir}/fonts/afm/public/pl/plsy8.afm
%{_texmfdistdir}/fonts/afm/public/pl/plsy9.afm
%{_texmfdistdir}/fonts/afm/public/pl/pltcsc10.afm
%{_texmfdistdir}/fonts/afm/public/pl/pltex10.afm
%{_texmfdistdir}/fonts/afm/public/pl/pltex8.afm
%{_texmfdistdir}/fonts/afm/public/pl/pltex9.afm
%{_texmfdistdir}/fonts/afm/public/pl/plti10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plti12.afm
%{_texmfdistdir}/fonts/afm/public/pl/plti7.afm
%{_texmfdistdir}/fonts/afm/public/pl/plti8.afm
%{_texmfdistdir}/fonts/afm/public/pl/plti9.afm
%{_texmfdistdir}/fonts/afm/public/pl/pltt10.afm
%{_texmfdistdir}/fonts/afm/public/pl/pltt12.afm
%{_texmfdistdir}/fonts/afm/public/pl/pltt8.afm
%{_texmfdistdir}/fonts/afm/public/pl/pltt9.afm
%{_texmfdistdir}/fonts/afm/public/pl/plu10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plvtt10.afm
%{_texmfdistdir}/fonts/enc/dvips/pl/plin.enc
%{_texmfdistdir}/fonts/enc/dvips/pl/plit.enc
%{_texmfdistdir}/fonts/enc/dvips/pl/plitt.enc
%{_texmfdistdir}/fonts/enc/dvips/pl/plme.enc
%{_texmfdistdir}/fonts/enc/dvips/pl/plmi.enc
%{_texmfdistdir}/fonts/enc/dvips/pl/plms.enc
%{_texmfdistdir}/fonts/enc/dvips/pl/plrm.enc
%{_texmfdistdir}/fonts/enc/dvips/pl/plsc.enc
%{_texmfdistdir}/fonts/enc/dvips/pl/plte.enc
%{_texmfdistdir}/fonts/enc/dvips/pl/pltt.enc
%{_texmfdistdir}/fonts/map/dvips/pl/plother.map
%{_texmfdistdir}/fonts/map/dvips/pl/pltext.map
%{_texmfdistdir}/fonts/source/public/pl/cmssbi10.mf
%{_texmfdistdir}/fonts/source/public/pl/dlr10.mf
%{_texmfdistdir}/fonts/source/public/pl/fik_mik.mf
%{_texmfdistdir}/fonts/source/public/pl/pl.mft
%{_texmfdistdir}/fonts/source/public/pl/pl_cud.mf
%{_texmfdistdir}/fonts/source/public/pl/pl_dl.mf
%{_texmfdistdir}/fonts/source/public/pl/pl_dod.mf
%{_texmfdistdir}/fonts/source/public/pl/pl_ml.mf
%{_texmfdistdir}/fonts/source/public/pl/pl_mlk.mf
%{_texmfdistdir}/fonts/source/public/pl/pl_sym.mf
%{_texmfdistdir}/fonts/source/public/pl/plb10.mf
%{_texmfdistdir}/fonts/source/public/pl/plbsy10.mf
%{_texmfdistdir}/fonts/source/public/pl/plbsy5.mf
%{_texmfdistdir}/fonts/source/public/pl/plbsy7.mf
%{_texmfdistdir}/fonts/source/public/pl/plbx10.mf
%{_texmfdistdir}/fonts/source/public/pl/plbx12.mf
%{_texmfdistdir}/fonts/source/public/pl/plbx5.mf
%{_texmfdistdir}/fonts/source/public/pl/plbx6.mf
%{_texmfdistdir}/fonts/source/public/pl/plbx7.mf
%{_texmfdistdir}/fonts/source/public/pl/plbx8.mf
%{_texmfdistdir}/fonts/source/public/pl/plbx9.mf
%{_texmfdistdir}/fonts/source/public/pl/plbxsl10.mf
%{_texmfdistdir}/fonts/source/public/pl/plbxti10.mf
%{_texmfdistdir}/fonts/source/public/pl/plcsc10.mf
%{_texmfdistdir}/fonts/source/public/pl/pldunh10.mf
%{_texmfdistdir}/fonts/source/public/pl/plex10.mf
%{_texmfdistdir}/fonts/source/public/pl/plff10.mf
%{_texmfdistdir}/fonts/source/public/pl/plfi10.mf
%{_texmfdistdir}/fonts/source/public/pl/plfib8.mf
%{_texmfdistdir}/fonts/source/public/pl/plinch.mf
%{_texmfdistdir}/fonts/source/public/pl/plitt10.mf
%{_texmfdistdir}/fonts/source/public/pl/plmi10.mf
%{_texmfdistdir}/fonts/source/public/pl/plmi12.mf
%{_texmfdistdir}/fonts/source/public/pl/plmi5.mf
%{_texmfdistdir}/fonts/source/public/pl/plmi6.mf
%{_texmfdistdir}/fonts/source/public/pl/plmi7.mf
%{_texmfdistdir}/fonts/source/public/pl/plmi8.mf
%{_texmfdistdir}/fonts/source/public/pl/plmi9.mf
%{_texmfdistdir}/fonts/source/public/pl/plmib10.mf
%{_texmfdistdir}/fonts/source/public/pl/plmib5.mf
%{_texmfdistdir}/fonts/source/public/pl/plmib7.mf
%{_texmfdistdir}/fonts/source/public/pl/plr10.mf
%{_texmfdistdir}/fonts/source/public/pl/plr12.mf
%{_texmfdistdir}/fonts/source/public/pl/plr17.mf
%{_texmfdistdir}/fonts/source/public/pl/plr5.mf
%{_texmfdistdir}/fonts/source/public/pl/plr6.mf
%{_texmfdistdir}/fonts/source/public/pl/plr7.mf
%{_texmfdistdir}/fonts/source/public/pl/plr8.mf
%{_texmfdistdir}/fonts/source/public/pl/plr9.mf
%{_texmfdistdir}/fonts/source/public/pl/plsl10.mf
%{_texmfdistdir}/fonts/source/public/pl/plsl12.mf
%{_texmfdistdir}/fonts/source/public/pl/plsl8.mf
%{_texmfdistdir}/fonts/source/public/pl/plsl9.mf
%{_texmfdistdir}/fonts/source/public/pl/plsltt10.mf
%{_texmfdistdir}/fonts/source/public/pl/plss10.mf
%{_texmfdistdir}/fonts/source/public/pl/plss12.mf
%{_texmfdistdir}/fonts/source/public/pl/plss17.mf
%{_texmfdistdir}/fonts/source/public/pl/plss8.mf
%{_texmfdistdir}/fonts/source/public/pl/plss9.mf
%{_texmfdistdir}/fonts/source/public/pl/plssbi10.mf
%{_texmfdistdir}/fonts/source/public/pl/plssbx10.mf
%{_texmfdistdir}/fonts/source/public/pl/plssdc10.mf
%{_texmfdistdir}/fonts/source/public/pl/plssi10.mf
%{_texmfdistdir}/fonts/source/public/pl/plssi12.mf
%{_texmfdistdir}/fonts/source/public/pl/plssi17.mf
%{_texmfdistdir}/fonts/source/public/pl/plssi8.mf
%{_texmfdistdir}/fonts/source/public/pl/plssi9.mf
%{_texmfdistdir}/fonts/source/public/pl/plssq8.mf
%{_texmfdistdir}/fonts/source/public/pl/plssqi8.mf
%{_texmfdistdir}/fonts/source/public/pl/plsy10.mf
%{_texmfdistdir}/fonts/source/public/pl/plsy5.mf
%{_texmfdistdir}/fonts/source/public/pl/plsy6.mf
%{_texmfdistdir}/fonts/source/public/pl/plsy7.mf
%{_texmfdistdir}/fonts/source/public/pl/plsy8.mf
%{_texmfdistdir}/fonts/source/public/pl/plsy9.mf
%{_texmfdistdir}/fonts/source/public/pl/pltcsc10.mf
%{_texmfdistdir}/fonts/source/public/pl/pltex10.mf
%{_texmfdistdir}/fonts/source/public/pl/pltex8.mf
%{_texmfdistdir}/fonts/source/public/pl/pltex9.mf
%{_texmfdistdir}/fonts/source/public/pl/plti10.mf
%{_texmfdistdir}/fonts/source/public/pl/plti12.mf
%{_texmfdistdir}/fonts/source/public/pl/plti7.mf
%{_texmfdistdir}/fonts/source/public/pl/plti8.mf
%{_texmfdistdir}/fonts/source/public/pl/plti9.mf
%{_texmfdistdir}/fonts/source/public/pl/pltt10.mf
%{_texmfdistdir}/fonts/source/public/pl/pltt12.mf
%{_texmfdistdir}/fonts/source/public/pl/pltt8.mf
%{_texmfdistdir}/fonts/source/public/pl/pltt9.mf
%{_texmfdistdir}/fonts/source/public/pl/plu10.mf
%{_texmfdistdir}/fonts/source/public/pl/plvtt10.mf
%{_texmfdistdir}/fonts/source/public/pl/polan.mf
%{_texmfdistdir}/fonts/source/public/pl/polkap.mf
%{_texmfdistdir}/fonts/source/public/pl/polkur.mf
%{_texmfdistdir}/fonts/source/public/pl/polmat.mf
%{_texmfdistdir}/fonts/source/public/pl/poltyt.mf
%{_texmfdistdir}/fonts/tfm/public/pl/plb10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plbsy10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plbsy5.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plbsy7.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plbx5.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plbx7.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plbxsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plbxti10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plcsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/pldunh10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plex10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plex9.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plff10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plfi10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plfib8.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plinch.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plitt10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plmi10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plmi12.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plmi5.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plmi6.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plmi7.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plmi8.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plmi9.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plmib10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plmib5.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plmib7.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plr10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plr12.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plr17.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plr5.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plr6.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plr7.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plr8.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plr9.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plsl12.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plsl8.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plsl9.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plsltt10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plss10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plss12.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plss17.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plss8.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plss9.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plssbi10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plssbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plssdc10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plssi10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plssi12.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plssi17.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plssi8.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plssi9.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plssq8.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plssqi8.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plsy10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plsy5.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plsy6.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plsy7.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plsy8.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plsy9.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/pltcsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/pltex10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/pltex8.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/pltex9.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plti10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plti12.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plti7.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plti8.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plti9.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/pltt10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/pltt12.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/pltt8.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/pltt9.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plu10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plvtt10.tfm
%{_texmfdistdir}/fonts/type1/public/pl/plb10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plb10.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plbsy10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plbsy10.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plbx10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plbx10.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plbx12.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plbx12.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plbx5.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plbx5.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plbx6.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plbx6.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plbx7.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plbx7.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plbx8.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plbx8.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plbx9.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plbx9.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plbxsl10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plbxsl10.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plbxti10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plbxti10.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plcsc10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plcsc10.pfm
%{_texmfdistdir}/fonts/type1/public/pl/pldunh10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/pldunh10.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plex10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plex10.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plex9.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plex9.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plff10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plff10.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plfi10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plfi10.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plfib8.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plfib8.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plinch.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plinch.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plitt10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plitt10.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plmi10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plmi10.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plmi12.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plmi12.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plmi5.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plmi5.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plmi6.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plmi6.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plmi7.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plmi7.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plmi8.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plmi8.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plmi9.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plmi9.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plmib10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plmib10.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plr10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plr10.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plr12.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plr12.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plr17.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plr17.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plr5.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plr5.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plr6.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plr6.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plr7.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plr7.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plr8.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plr8.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plr9.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plr9.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plsl10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plsl10.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plsl12.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plsl12.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plsl8.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plsl8.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plsl9.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plsl9.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plsltt10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plsltt10.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plss10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plss10.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plss12.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plss12.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plss17.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plss17.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plss8.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plss8.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plss9.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plss9.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plssbi10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plssbi10.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plssbx10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plssbx10.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plssdc10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plssdc10.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plssi10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plssi10.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plssi12.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plssi12.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plssi17.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plssi17.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plssi8.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plssi8.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plssi9.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plssi9.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plssq8.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plssq8.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plssqi8.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plssqi8.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plsy10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plsy10.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plsy5.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plsy5.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plsy6.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plsy6.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plsy7.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plsy7.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plsy8.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plsy8.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plsy9.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plsy9.pfm
%{_texmfdistdir}/fonts/type1/public/pl/pltcsc10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/pltcsc10.pfm
%{_texmfdistdir}/fonts/type1/public/pl/pltex10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/pltex10.pfm
%{_texmfdistdir}/fonts/type1/public/pl/pltex8.pfb
%{_texmfdistdir}/fonts/type1/public/pl/pltex8.pfm
%{_texmfdistdir}/fonts/type1/public/pl/pltex9.pfb
%{_texmfdistdir}/fonts/type1/public/pl/pltex9.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plti10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plti10.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plti12.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plti12.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plti7.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plti7.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plti8.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plti8.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plti9.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plti9.pfm
%{_texmfdistdir}/fonts/type1/public/pl/pltt10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/pltt10.pfm
%{_texmfdistdir}/fonts/type1/public/pl/pltt12.pfb
%{_texmfdistdir}/fonts/type1/public/pl/pltt12.pfm
%{_texmfdistdir}/fonts/type1/public/pl/pltt8.pfb
%{_texmfdistdir}/fonts/type1/public/pl/pltt8.pfm
%{_texmfdistdir}/fonts/type1/public/pl/pltt9.pfb
%{_texmfdistdir}/fonts/type1/public/pl/pltt9.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plu10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plu10.pfm
%{_texmfdistdir}/fonts/type1/public/pl/plvtt10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plvtt10.pfm
%_texmf_updmap_d/pl
%doc %{_texmfdistdir}/doc/fonts/pl/README-T1.ENG
%doc %{_texmfdistdir}/doc/fonts/pl/README-T1.POL
%doc %{_texmfdistdir}/doc/fonts/pl/README.ENG
%doc %{_texmfdistdir}/doc/fonts/pl/README.POL
%doc %{_texmfdistdir}/doc/fonts/pl/plsample.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/pl <<EOF
MixedMap plother.map
MixedMap pltext.map
EOF


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.15-2
+ Revision: 754959
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.15-1
+ Revision: 719267
- texlive-pl
- texlive-pl
- texlive-pl
- texlive-pl

