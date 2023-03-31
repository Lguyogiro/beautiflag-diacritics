# beautiflag-diacritics

Define flag diacritics as macros, place them at the end of the relevant lines only, and compile to fst via lexc.

#### Define flag diacritics as macros at top of lexb file. e.g.
```
Define_Flags
[P Plural Subj] @P.SubjPl.1@
[R Plural Subj] @R.SubjPl.1@
[D Plural Subj] @D.SubjPl@

[P Past] @P.IsPast.1@
[R Past] @R.IsPast.1@
[D Past] @D.IsPast@

[P Optative] @P.Opt.1@
[R Optative] @R.Opt@
[D Optative] @D.Opt@
End Define_Flags

```

#### When you want to use a flag diacritic, just add the defined macro somewhere on the line:

```
LEXICON SujetoVerbal

%<s_sg1%>:ni%>    SujetoCont ;
%<s_sg1%>:ni%>    SujetoCont ; [P Optative]
...
%<s_pl1%>:ti%>    SujetoCont ; [P Plural Subj]
%<s_pl1%>:ti%>    SujetoCont ; [P Plural Subj] [P Optative]

%<s_pl2%>:nan%>   SujetoCont ; [P Plural Subj]
%<s_pl3%>:0%>     SujetoCont ; [P Plural Subj]
%<s_pl3%>:0%>     SujetoCont ; [P Plural Subj] [P Optative]

%<s_sg2%>:xi%>    SujetoCont ; [P Optative]
%<s_pl2%>:xi%>    SujetoCont ; [P Plural Subj] [P Optative]

```

compile your fst:
`./lexb.sh <something>.lexb <something>.hfst`
