import argparse
from antlr4 import FileStream, CommonTokenStream, ParseTreeListener, ParseTreeWalker
from scasm.scasmLexer import scasmLexer
from scasm.scasmParser import scasmParser

DEBUG = True

symboltable = dict()
ast = []
currentRamAddr = 0

class scasmListener(ParseTreeListener):
    def enterScasmProg(self, ctx: scasmParser.ScasmProgContext):
        DEBUG and print('====== Start Parsing and Abstract Syntax List (LOL) Generation ======')
        symboltable = {}
        ast = []
        currentRamAddr = 0
        pass

    # Exit a parse tree produced by scasmParser#scasmProg.
    def exitScasmProg(self, ctx: scasmParser.ScasmProgContext):
        pass

    # Exit a parse tree produced by scasmParser#scasmLine.
    def exitScasmLine(self, ctx: scasmParser.ScasmLineContext):
        if ctx.label() is not None:
            label = ctx.label().label
            DEBUG and print('Label: %s = 0x%04X' % (label, currentRamAddr))
            if label in symboltable:
                sym = ctx.label().ID().symbol
                print('WARN: Label redefinition (%s) at line %d:%d' % (label, sym.line, sym.column))
            else:
                symboltable[label] = currentRamAddr
        pass

    # Enter a parse tree produced by scasmParser#label.
    def enterLabel(self, ctx: scasmParser.LabelContext):
        ctx.label = str(ctx.ID())
        pass

    # Exit a parse tree produced by scasmParser#label.
    def exitLabel(self, ctx: scasmParser.LabelContext):
        pass

    # Enter a parse tree produced by scasmParser#directive.
    def enterDirective(self, ctx: scasmParser.DirectiveContext):
        pass

    # Exit a parse tree produced by scasmParser#directive.
    def exitDirective(self, ctx: scasmParser.DirectiveContext):
        pass

    # Enter a parse tree produced by scasmParser#directiveDW.
    def enterDirectiveDW(self, ctx: scasmParser.DirectiveDWContext):
        pass

    # Exit a parse tree produced by scasmParser#directiveDW.
    def exitDirectiveDW(self, ctx: scasmParser.DirectiveDWContext):
        pass

    # Enter a parse tree produced by scasmParser#directiveORG.
    def enterDirectiveORG(self, ctx: scasmParser.DirectiveORGContext):
        pass

    # Exit a parse tree produced by scasmParser#directiveORG.
    def exitDirectiveORG(self, ctx: scasmParser.DirectiveORGContext):
        pass

    # Enter a parse tree produced by scasmParser#directiveEQU.
    def enterDirectiveEQU(self, ctx: scasmParser.DirectiveEQUContext):
        pass

    # Exit a parse tree produced by scasmParser#directiveEQU.
    def exitDirectiveEQU(self, ctx: scasmParser.DirectiveEQUContext):
        pass

    # Enter a parse tree produced by scasmParser#argList.
    def enterArgList(self, ctx: scasmParser.ArgListContext):
        pass

    # Exit a parse tree produced by scasmParser#argList.
    def exitArgList(self, ctx: scasmParser.ArgListContext):
        pass

    # Enter a parse tree produced by scasmParser#argListTail.
    def enterArgListTail(self, ctx: scasmParser.ArgListTailContext):
        pass

    # Exit a parse tree produced by scasmParser#argListTail.
    def exitArgListTail(self, ctx: scasmParser.ArgListTailContext):
        pass

    # Enter a parse tree produced by scasmParser#instruction.
    def enterInstruction(self, ctx: scasmParser.InstructionContext):
        pass

    # Exit a parse tree produced by scasmParser#instruction.
    def exitInstruction(self, ctx: scasmParser.InstructionContext):
        pass

    # Enter a parse tree produced by scasmParser#constantArgument.
    def enterConstantArgument(self, ctx: scasmParser.ConstantArgumentContext):
        pass

    # Exit a parse tree produced by scasmParser#constantArgument.
    def exitConstantArgument(self, ctx: scasmParser.ConstantArgumentContext):
        pass

    # Enter a parse tree produced by scasmParser#expr.
    def enterExpr(self, ctx: scasmParser.ExprContext):
        pass

    # Exit a parse tree produced by scasmParser#expr.
    def exitExpr(self, ctx: scasmParser.ExprContext):
        pass

    # Enter a parse tree produced by scasmParser#exprTail.
    def enterExprTail(self, ctx: scasmParser.ExprTailContext):
        pass

    # Exit a parse tree produced by scasmParser#exprTail.
    def exitExprTail(self, ctx: scasmParser.ExprTailContext):
        pass

    # Exit a parse tree produced by scasmParser#labelRef.
    def exitLabelRef(self, ctx: scasmParser.LabelRefContext):
        pass

    # Exit a parse tree produced by scasmParser#integer.
    def exitInteger(self, ctx: scasmParser.IntegerContext):
        if ctx.INT_BIN() is not None:
            ctx.value = int(str(ctx.INT_BIN()), 2)
        elif ctx.INT_HEX() is not None:
            hexStr = str(ctx.INT_HEX()).replace('&H', '0x')
            ctx.value = int(hexStr, 16)
        elif ctx.INT_DEC() is not None:
            ctx.value = int(str(ctx.INT_DEC()), 10)
        else:
            print('wtf number is this????')
            exit(-1)
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple Computer Turbo Assembler')
    parser.add_argument('file', type=str)

    args = parser.parse_args()
    print('Simple Computer Turbo Assembler 9000')
    print('        Brought to you by Gangweed Ganggang :D)))')

    filename = args.file
    input = FileStream(filename)
    lexer = scasmLexer(input)
    stream = CommonTokenStream(lexer)
    parser = scasmParser(stream)

    tree = parser.scasmProg()

    listener = scasmListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    print('====== First Pass Symbol Table ======')
    print(symboltable)

    pass
