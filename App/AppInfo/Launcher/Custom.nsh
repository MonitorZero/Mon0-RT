${SegmentFile}

Var bolCustomRegistryExists

${SegmentPrePrimary}
	StrCpy $bolCustomRegistryExists false
    ${If} $Bits == 64
		SetRegView 64
		ReadRegStr $0 HKLM "SOFTWARE\Piriform\CCleaner" "(Cfg)LastUpdate"
		${If} $0 != ""
			StrCpy $bolCustomRegistryExists true
		${EndIf}
		SetRegView 32
	${EndIf}
!macroend

${SegmentPostPrimary}
    ${If} $Bits == 64
	${AndIf} $bolCustomRegistryExists == false
		SetRegView 64
			DeleteRegKey HKLM "SOFTWARE\Piriform\CCleaner"
			DeleteRegKey /ifempty HKLM "SOFTWARE\Piriform"
		SetRegView 32
	${EndIf}
!macroend