grammar scasm;

scasmProg: scasmLine? scasmLines EOF;
scasmLines: | EOL scasmLine? scasmLines;

scasmLine: label? (directive|instruction);
label: ID COLON;

directive: (directiveDW | directiveORG | directiveEQU);
directiveDW: DIR_DW constantArgument;
directiveORG: DIR_ORG constantArgument;
directiveEQU: label DIR_EQU constantArgument;

argList: | constantArgument argListTail;
argListTail: COMMA argList |;
instruction: OpCode argList;

constantArgument: expr;

expr: (integer | labelRef) exprTail
    | LPARN expr RPARN exprTail;
exprTail: | binaryOperator expr;

binaryOperator: ADD | SUB;

labelRef: ID;

integer: INT_HEX | INT_DEC | INT_BIN;
INT_HEX: ('0x'|'0X'|'&H'|'&h')[0-9A-Fa-f]+;
INT_BIN: '0b'[0-1]+;
INT_DEC: [0-9]+;

White_Space: [ \t]+ -> skip;
EOL: [\r\n]+;
COLON: ':';
SEMI: ';';
LPARN: '(';
RPARN: ')';
COMMA: ',';
ADD: '+';
SUB: '-';

// Really toxic but well
fragment A : [aA]; // match either an 'a' or 'A'
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];

DIR_EQU: E Q U;
DIR_DW: D W;
DIR_ORG: O R G;

OpCode: OpNOP
| OpLOAD
| OpSTORE
| OpADD
| OpSUB
| OpJUMP
| OpJNEG
| OpJPOS
| OpJZERO
| OpAND
| OpOR
| OpXOR
| OpSHIFT
| OpADDI
| OpILOAD
| OpISTORE
| OpCALL
| OpRETURN
| OpIN
| OpOUT;

OpNOP: N O P;
OpLOAD: L O A D;
OpSTORE: S T O R E;
OpADD: A D D;
OpSUB: S U B;
OpJUMP: J U M P;
OpJNEG: J N E G;
OpJPOS: J P O S;
OpJZERO: J Z E R O;
OpAND: A N D;
OpOR: O R;
OpXOR: X O R;
OpSHIFT: S H I F T;
OpADDI: A D D I;
OpILOAD: I L O A D;
OpISTORE: I S T O R E;
OpCALL: C A L L;
OpRETURN: R E T U R N;
OpIN: I N;
OpOUT: O U T;

ID: [a-zA-Z_$%][a-zA-Z0-9_$%]*;

