## Full_verified suite — spreadsheetbench  (held-out test split)

Agent `ibm-rits/google/gemma-4-31B-it` · optimizer Claude Code `ibm-rits/google/gemma-4-31B-it` · 0 iteration(s) · base→opt is the seed vs the best candidate on the **same 280 SEALED test tasks**, which the optimizer never saw (selection happened on a disjoint val split). This is a held-out generalization number.

| bench | task | reward (base→opt) | Δ | note |
|---|---|---|---|:--:|
| spreadsheetbench | `13-1` | 0.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `17-35` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `23-24` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `24-23` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `28-7` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `41-47` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `60-7` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `267-21` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `269-43` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `269-44` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `279-23` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `280-17` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `283-32` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `290-1` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `290-27` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `297-42` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `304-35` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `333-29` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `341-40` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `384-4` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `408-5` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `455-35` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `469-9` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `477-45` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `547-18` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `61-4` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `73-45` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `79-7` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `82-38` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `84-40` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `91-34` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `97-36` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `109-21` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `130-9` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `142-19` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `146-49` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `147-48` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `156-14` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `157-4` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `160-6` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `168-17` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `177-6` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `178-22` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `191-40` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `203-15` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `208-20` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `230-16` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `236-22` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `120-24` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `183-8` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `188-39` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `209-30` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `302-1` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `334-11` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `341-14` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `343-20` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `353-6` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `353-29` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `359-21` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `367-23` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `374-18` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `374-31` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `382-29` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `387-16` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `388-47` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `399-14` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `409-45` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `416-27` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `423-16` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `438-18` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `440-24` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `448-11` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `486-17` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `488-14` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `493-5` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `496-15` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `496-34` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `510-3` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `516-46` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `524-31` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `531-18` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `534-26` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `535-20` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `545-35` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `547-43` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `567-21` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `599-9` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `12307` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `15380` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `31202` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `33722` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `37900` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `38074` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `38537` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `38703` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `38823` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `38969` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `38985` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `39432` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `39515` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `39667` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `40478` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `41410` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `41601` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `41691` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `41969` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `42198` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `42526` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `44389` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `45300` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `45896` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `46167` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `46240` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `47842` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `47933` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `48257` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `48608` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `48643` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `48924` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `48969` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `48975` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `48982` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `49036` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `49196` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `49237` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `49300` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `49667` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `49801` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `50088` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `50193` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `50324` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `50526` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `50682` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `50796` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `50952` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `51262` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `51289` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `51359` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `51431` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `51586` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `52575` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `52807` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `52917` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `53167` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `54196` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `54242` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `54590` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `54675` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `1563` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `1925` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `3002` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `3911` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `4714` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `5835` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `7665` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `9111` | 0.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `9391` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `9448` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `11276` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `13284` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `14240` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `15387` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `15671` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `16511` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `17111` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `18645` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `18935` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `31746` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `32093` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `32293` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `32562` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `32789` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `33157` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `34210` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `35739` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `35747` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `36191` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `36764` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `37086` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `37229` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `37462` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `37554` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `36277` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `39190` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `40757` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `40959` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `41265` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `41348` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `41420` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `41589` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `41978` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `42181` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `42216` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `42515` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `42930` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `44266` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `44296` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `44628` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `45063` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `45738` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `45944` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `49857` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `49945` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `50051` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `50250` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `50486` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `50521` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `50631` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `50683` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `50811` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `50971` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `51354` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `51556` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `51680` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `52050` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `52220` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `52233` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `52305` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `52532` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `52541` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `52964` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `53117` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `53161` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `53449` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `53994` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `54274` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `54474` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `54513` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `54667` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `54717` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `54925` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `55085` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `55817` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `56225` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `56378` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `56419` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `56599` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `56920` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `56921` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `57033` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `57232` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `57590` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `58147` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `58701` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `58723` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `42902` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `43213` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `43657` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `44017` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `44913` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `45707` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `45937` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `47827` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `55260` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `55468` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `55708` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `55976` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `55977` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `56915` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `56953` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `57117` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `57262` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `57354` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `57612` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `57693` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `57989` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `58032` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `58687` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `58904` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `58942` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `59129` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `59160` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `59224` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `59358` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `59511` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `59639` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `59734` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `59794` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `59884` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `59902` | 1.000 → 1.000 | +0.000 |  |

**Suite (held-out):** mean reward 0.579 → 0.579 (Δ +0.000 (+0% rel)) · best = seed (no candidate beat baseline) · optimizer $0.00 over 0 iter(s) · 2 task(s) infra-errored

> No candidate was accepted, so base→opt is the seed against itself and Δ is 0.000 by construction. Re-scoring those same bytes for the finalize read 0.579 against the baseline's 0.579 — a spread of 0.000. That is this tier's re-measurement **noise**, not a change in the capability, and it is the floor any real effect here would have to clear.

### Metrics by candidate and split

| candidate | split | n | `soft_restriction` | `hard_restriction` | `soft_no_recalc` | `hard_no_recalc` |
|---|---|--:|--:|--:|--:|--:|
| seed | train | 80 | 0.5875 | 0.5875 | 0.5875 | 0.5875 |
| seed | val | 38 | 0.6579 | 0.6579 | 0.6579 | 0.6579 |
| seed | test | 278 | 0.5755 | 0.5755 | 0.5791 | 0.5791 |
| best | train | 80 | 0.5875 | 0.5875 | 0.5875 | 0.5875 |
| best | val | 38 | 0.6579 | 0.6579 | 0.6579 | 0.6579 |
| best | test | 278 | 0.5755 | 0.5755 | 0.5791 | 0.5791 |

### Iterations

| phase | iter | candidate | accepted | reward | optimizer $ | optimizer time | eval $ | eval time |
|---|:--:|---|:--:|---|---|---|---|---|
| baseline | — | `seed` | — | 0.658 | $0.0000 | 0s | $0.0000 | 15m08s |
| finalize | — | `seed` | — | 0.579 | $0.0000 | 0s | $0.0000 | 99m14s |

**Totals:** optimizer $0.0000 over 0s · eval $0.0000 over 114m22s
