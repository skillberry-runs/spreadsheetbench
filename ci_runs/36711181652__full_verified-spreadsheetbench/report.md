## Full_verified suite — spreadsheetbench  (held-out test split)

Agent `ibm-ete-int/azure/gpt-5.5` · optimizer Claude Code `ibm-ete-int/aws/claude-opus-5` · 5 iteration(s) · base→opt is the seed vs the best candidate on the **same 280 SEALED test tasks**, which the optimizer never saw (selection happened on a disjoint val split). This is a held-out generalization number.

| bench | task | reward (base→opt) | Δ | note |
|---|---|---|---|:--:|
| spreadsheetbench | `13-1` | 1.000 → 1.000 | +0.000 |  |
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
| spreadsheetbench | `455-35` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `469-9` | 1.000 → 0.000 | -1.000 | ↓ |
| spreadsheetbench | `477-45` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `547-18` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `61-4` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `73-45` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `79-7` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `82-38` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `84-40` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `91-34` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `97-36` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `109-21` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `130-9` | 0.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `142-19` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `146-49` | 0.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `147-48` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `156-14` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `157-4` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `160-6` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `168-17` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `177-6` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `178-22` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `191-40` | 0.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `203-15` | 0.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `208-20` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `230-16` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `236-22` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `120-24` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `183-8` | 0.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `188-39` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `209-30` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `302-1` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `334-11` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `341-14` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `343-20` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `353-6` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `353-29` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `359-21` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `367-23` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `374-18` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `374-31` | 0.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `382-29` | 0.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `387-16` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `388-47` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `399-14` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `409-45` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `416-27` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `423-16` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `438-18` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `440-24` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `448-11` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `486-17` | 0.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `488-14` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `493-5` | 0.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `496-15` | 0.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `496-34` | 0.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `510-3` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `516-46` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `524-31` | 1.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `531-18` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `534-26` | 0.000 → ⚠️ infra-error | — | ⚠️ |
| spreadsheetbench | `535-20` | 1.000 → ⚠️ infra-error | — | ⚠️ |
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
| spreadsheetbench | `45300` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `45896` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `46167` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `46240` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `47842` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `47933` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `48257` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `48608` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `48643` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `48924` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `48969` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `48975` | 0.000 → 1.000 | +1.000 |  |
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
| spreadsheetbench | `52575` | 1.000 → 1.000 | +0.000 |  |
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
| spreadsheetbench | `4714` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `5835` | 0.000 → 0.000 | +0.000 |  |
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
| spreadsheetbench | `32562` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `32789` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `33157` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `34210` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `35739` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `35747` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `36191` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `36764` | 1.000 → 1.000 | +0.000 |  |
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
| spreadsheetbench | `41420` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `41589` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `41978` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `42181` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `42216` | 1.000 → 0.000 | -1.000 | ↓ |
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
| spreadsheetbench | `50051` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `50250` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `50486` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `50521` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `50631` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `50683` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `50811` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `50971` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `51354` | 1.000 → 1.000 | +0.000 |  |
| spreadsheetbench | `51556` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `51680` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `52050` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `52220` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `52233` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `52305` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `52532` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `52541` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `52964` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `53117` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `53161` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `53449` | 0.000 → 1.000 | +1.000 |  |
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
| spreadsheetbench | `57033` | 1.000 → 1.000 | +0.000 |  |
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
| spreadsheetbench | `55977` | 0.000 → 1.000 | +1.000 |  |
| spreadsheetbench | `56915` | 0.000 → 0.000 | +0.000 |  |
| spreadsheetbench | `56953` | 0.000 → 1.000 | +1.000 |  |
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

**Suite (held-out):** mean reward 0.386 → 0.898 (Δ +0.512 (+133% rel)) · best = `cand_0001` · optimizer $83.87 over 5 iter(s) · 55 task(s) infra-errored

### Metrics by candidate and split

| candidate | split | n | `soft_restriction` | `hard_restriction` | `soft_no_recalc` | `hard_no_recalc` |
|---|---|--:|--:|--:|--:|--:|
| seed | train | 80 | 0.7875 | 0.7875 | 0.4000 | 0.4000 |
| seed | val | 40 | 0.7250 | 0.7250 | 0.3000 | 0.3000 |
| seed | test | 280 | 0.7750 | 0.7750 | 0.3857 | 0.3857 |
| best | train | 80 | 0.9125 | 0.9125 | 0.9250 | 0.9250 |
| best | val | 40 | 0.9750 | 0.9750 | 0.9750 | 0.9750 |
| best | test | 225 | 0.9022 | 0.9022 | 0.8978 | 0.8978 |

### Iterations

| phase | iter | candidate | accepted | reward | traded | optimizer $ | optimizer time | eval $ | eval time |
|---|:--:|---|:--:|---|---|---|---|---|---|
| iterate | 1 | `cand_0001` | ✅ | 0.975 | +27 fixed / -0 broke | $20.4974 | 82m51s | $2.2113 | 4m11s |
| iterate | 2 | `cand_0002` | ❌ | 0.875 | +0 fixed / -4 broke | $14.4769 | 60m01s | $2.2844 | 5m20s |
| iterate | 3 | `cand_0003` | ❌ | 0.925 | +1 fixed / -3 broke | $14.5720 | 57m17s | $2.6564 | 5m19s |
| iterate | 4 | `cand_0004` | ❌ | 0.975 | +1 fixed / -1 broke | $18.6114 | 47m42s | $2.0800 | 5m10s |
| iterate | 5 | `cand_0005` | ❌ | 0.975 | +1 fixed / -1 broke | $15.7112 | 70m29s | $1.7984 | 5m30s |
| finalize | — | `cand_0001` | — | 0.898 | — | $0.0000 | 0s | $18.4212 | 42m54s |
| unattributed | — | `(whole run)` | — | — | — | $0.0000 | 0s | $6.6503 | 18m55s |

**Totals:** optimizer $83.8689 over 318m20s · eval $36.1021 over 87m18s

> The `unattributed` row is metered spend no phase above owns (eval $6.6503 — control replicates, re-gates and abandoned rounds are real evaluations that no committed step references). It is shown rather than dropped so these totals match what the run actually paid: `spent` reads $36.10 runner + $83.87 optimizer.
