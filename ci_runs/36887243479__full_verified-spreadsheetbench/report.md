## Full_verified suite — spreadsheetbench  (held-out test split)

Agent `ibm-ete/azure/gpt-5.5` · optimizer Claude Code `ibm-ete/aws/claude-opus-5` · 5 iteration(s) · base→opt is the seed vs the best candidate on the **same 280 SEALED test tasks**, which the optimizer never saw (selection happened on a disjoint val split). This is a held-out generalization number.

| bench | task | reward (base→opt) | Δ | note |
|---|---|---|---|:--:|
| spreadsheetbench | `13-1` | 1.000 → 0.000 | -1.000 | ↓ |
| spreadsheetbench | `17-35` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `23-24` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `24-23` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `28-7` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `41-47` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `60-7` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `267-21` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `269-43` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `269-44` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `279-23` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `280-17` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `283-32` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `290-1` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `290-27` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `297-42` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `304-35` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `333-29` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `341-40` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `384-4` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `408-5` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `455-35` | 1.000 → 0.000 | -1.000 | ↓ |
| spreadsheetbench | `469-9` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `477-45` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `547-18` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `61-4` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `73-45` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `79-7` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `82-38` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `84-40` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `91-34` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `97-36` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `109-21` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `130-9` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `142-19` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `146-49` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `147-48` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `156-14` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `157-4` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `160-6` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `168-17` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `177-6` | 1.000 → 0.000 | -1.000 | ↓ |
| spreadsheetbench | `178-22` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `191-40` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `203-15` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `208-20` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `230-16` | 1.000 → 0.000 | -1.000 | ↓ |
| spreadsheetbench | `236-22` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `120-24` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `183-8` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `188-39` | 1.000 → 0.000 | -1.000 | ↓ |
| spreadsheetbench | `209-30` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `302-1` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `334-11` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `341-14` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `343-20` | 1.000 → 0.000 | -1.000 | ↓ |
| spreadsheetbench | `353-6` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `353-29` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `359-21` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `367-23` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `374-18` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `374-31` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `382-29` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `387-16` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `388-47` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `399-14` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `409-45` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `416-27` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `423-16` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `438-18` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `440-24` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `448-11` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `486-17` | 1.000 → 0.000 | -1.000 | ↓ |
| spreadsheetbench | `488-14` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `493-5` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `496-15` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `496-34` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `510-3` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `516-46` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `524-31` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `531-18` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `534-26` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `535-20` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `545-35` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `547-43` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `567-21` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `599-9` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `12307` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `15380` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `31202` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `33722` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `37900` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `38074` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `38537` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `38703` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `38823` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `38969` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `38985` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `39432` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `39515` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `39667` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `40478` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `41410` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `41601` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `41691` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `41969` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `42198` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `42526` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `44389` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `45300` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `45896` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `46167` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `46240` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `47842` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `47933` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `48257` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `48608` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `48643` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `48924` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `48969` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `48975` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `48982` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `49036` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `49196` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `49237` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `49300` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `49667` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `49801` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `50088` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `50193` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `50324` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `50526` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `50682` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `50796` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `50952` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `51262` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `51289` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `51359` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `51431` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `51586` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `52575` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `52807` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `52917` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `53167` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `54196` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `54242` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `54590` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `54675` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `1563` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `1925` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `3002` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `3911` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `4714` | 1.000 → 0.000 | -1.000 | ↓ |
| spreadsheetbench | `5835` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `7665` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `9111` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `9391` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `9448` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `11276` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `13284` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `14240` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `15387` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `15671` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `16511` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `17111` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `18645` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `18935` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `31746` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `32093` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `32293` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `32562` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `32789` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `33157` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `34210` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `35739` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `35747` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `36191` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `36764` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `37086` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `37229` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `37462` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `37554` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `36277` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `39190` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `40757` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `40959` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `41265` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `41348` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `41420` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `41589` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `41978` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `42181` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `42216` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `42515` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `42930` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `44266` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `44296` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `44628` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `45063` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `45738` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `45944` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `49857` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `49945` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `50051` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `50250` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `50486` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `50521` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `50631` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `50683` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `50811` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `50971` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `51354` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `51556` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `51680` | 1.000 → 0.000 | -1.000 | ↓ |
| spreadsheetbench | `52050` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `52220` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `52233` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `52305` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `52532` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `52541` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `52964` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `53117` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `53161` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `53449` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `53994` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `54274` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `54474` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `54513` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `54667` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `54717` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `54925` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `55085` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `55817` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `56225` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `56378` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `56419` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `56599` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `56920` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `56921` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `57033` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `57232` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `57590` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `58147` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `58701` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `58723` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `42902` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `43213` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `43657` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `44017` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `44913` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `45707` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `45937` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `47827` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `55260` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `55468` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `55708` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `55976` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `55977` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `56915` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `56953` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `57117` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `57262` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `57354` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `57612` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `57693` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `57989` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `58032` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `58687` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `58904` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `58942` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `59129` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `59160` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `59224` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `59358` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `59511` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `59639` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `59734` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `59794` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `59884` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `59902` | 0.000 → 1.000 | +1.000 |  |

**Suite (held-out):** mean reward 0.386 → 0.871 (Δ +0.485 (+126% rel)) · best = `cand_0002` · optimizer $22.74 over 5 iter(s) · 1 task(s) infra-errored

### Metrics by candidate and split

| candidate | split | n | `soft_restriction` | `hard_restriction` | `soft_no_recalc` | `hard_no_recalc` |
|---|---|--:|--:|--:|--:|--:|
| seed | train | 80 | 0.7750 | 0.7750 | 0.3750 | 0.3750 |
| seed | val | 40 | 0.7500 | 0.7500 | 0.3500 | 0.3500 |
| seed | test | 280 | 0.7750 | 0.7750 | 0.3857 | 0.3857 |
| best | train | 80 | 0.8625 | 0.8625 | 0.8625 | 0.8625 |
| best | val | 40 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| best | test | 279 | 0.8710 | 0.8710 | 0.8710 | 0.8710 |

### Iterations

| phase | iter | candidate | accepted | reward | traded | optimizer $ | optimizer time | eval $ | eval time |
|---|:--:|---|:--:|---|---|---|---|---|---|
| iterate | 1 | `cand_0001` | ✅ | 0.950 | +24 fixed / -0 broke | $4.5821 | 20m55s | $4.0072 | 5m33s |
| iterate | 2 | `cand_0002` | ✅ | 1.000 | +2 fixed / -0 broke | $7.5439 | 19m34s | $4.3119 | 7m28s |
| iterate | 3 | `cand_0003` | ❌ | 0.975 | +0 fixed / -1 broke | $2.4243 | 8m22s | $4.4162 | 5m48s |
| iterate | 4 | `cand_0004` | ❌ | 1.000 | — | $1.3961 | 5m19s | $4.1465 | 5m44s |
| iterate | 5 | `cand_0005` | ❌ | 1.000 | — | $6.7942 | 15m39s | $3.7491 | 5m46s |
| finalize | — | `cand_0002` | — | 0.871 | — | $0.0000 | 0s | $44.1884 | 39m38s |
| unattributed | — | `(whole run)` | — | — | — | $0.0000 | 0s | $10.6570 | 11m50s |

**Totals:** optimizer $22.7407 over 69m49s · eval $75.4763 over 81m47s

> The `unattributed` row is metered spend no phase above owns (optimizer $0.0000 — agent mode runs ONE optimizer process, metered whole-loop, so no round owns a share of it; eval $10.6570 — control replicates, re-gates and abandoned rounds are real evaluations that no committed step references). It is shown rather than dropped so these totals match what the run actually paid: `spent` reads $75.48 runner + $22.74 optimizer.
