# Generate automatically
from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):
    # program: SKIP_* variable_decl* SKIP_* body_decl* SKIP_* EOF;
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        program = []
        if ctx.variable_decl():
            program += [y for x in ctx.variable_decl() for y in x.accept(self)]
        if ctx.body_decl():
            program += [x.accept(self) for x in ctx.body_decl()]
        return Program(program)

    # variable_decl: VAR COLON variable_list SEMI;
    def visitVariable_decl(self, ctx:BKITParser.Variable_declContext):
        return ctx.variable_list().accept(self)

    # variable_list: variable (ASSIGN init_value)? COMMA variable_list | variable (ASSIGN init_value)?;
    def visitVariable_list(self, ctx:BKITParser.Variable_listContext):
        var, dimen = ctx.variable().accept(self)
        init = []
        if ctx.variable_list():
            if ctx.init_value():
                init = ctx.init_value().accept(self)
            return [VarDecl(var, dimen, init)] + ctx.variable_list().accept(self)
        else:
            if ctx.init_value():
                init = ctx.init_value().accept(self)
            return [VarDecl(var, dimen, init)]

    # variable: ID | array_decl;
    def visitVariable(self, ctx:BKITParser.VariableContext):
        if ctx.ID():
            return (Id(ctx.ID().getText()),[])
        return ctx.array_decl().accept(self)

    # array_decl: ID dimension;
    def visitArray_decl(self, ctx:BKITParser.Array_declContext):
        return (Id(ctx.ID().getText()), ctx.dimension().accept(self))

    # dimension: LEFT_BRACKET integer RIGHT_BRACKET dimension | LEFT_BRACKET integer RIGHT_BRACKET;
    def visitDimension(self, ctx:BKITParser.DimensionContext):
        if ctx.getChildCount() > 3:
            return [ctx.integer().accept(self)] + ctx.dimension().accept(self)
        return [ctx.integer().accept(self)]

    # init_value: literal COMMA init_value | literal;
    def visitInit_value(self, ctx:BKITParser.Init_valueContext):
        if ctx.init_value():
            return ctx.literal().accept(self) + ctx.init_value().accept(self)
        return ctx.literal().accept(self)

    # literal: array | integer | FLOAT  | boolean_literal | STRING;
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        if ctx.array():
            return ArrayLiteral(ctx.array().accept(self))
        elif ctx.integer():
            return IntLiteral(ctx.integer().accept(self))
        elif ctx.FLOAT():
            return FloatLiteral(float(ctx.FLOAT().getText()))
        elif ctx.boolean_literal():
            return BooleanLiteral(ctx.boolean_literal().accept(self))
        elif ctx.STRING():
            return StringLiteral(ctx.STRING().getText())

    # integer: DECIMAL_INTEGER | HEX_INTEGER | OCT_INTEGER;
    def visitInteger(self, ctx:BKITParser.IntegerContext):
        return eval(ctx.getText())

    # boolean_literal: TRUE | FALSE ;
    def visitBoolean_literal(self, ctx:BKITParser.Boolean_literalContext):
        return ctx.getText()

    # array: LEFT_BRACE array_list? RIGHT_BRACE;
    def visitArray(self, ctx:BKITParser.ArrayContext):
        arrayList = []
        if ctx.array_list():
            arrayList += ctx.array_list().accept(self)
        return arrayList

    # array_list: literal COMMA array_list | literal;
    def visitArray_list(self, ctx:BKITParser.Array_listContext):
        if ctx.getChildCount() == 1:
            return [ctx.literal().accept(self)]
        return [ctx.literal().accept(self)] + ctx.array_list().accept(self)

    # body_decl: init_body body;
    def visitBody_decl(self, ctx:BKITParser.Body_declContext):
        name, param = ctx.init_body().accept(self)
        body = ctx.body().accept(self)
        return FuncDecl(name, param, body)

    # init_body: FUNCTION COLON ID parameter?;
    def visitInit_body(self, ctx:BKITParser.Init_bodyContext):
        name = Id(ctx.ID().getText())
        param = []
        if ctx.parameter():
            param += ctx.parameter().accept(self)
        return (name, param)

    # parameter: PARAMETER COLON parameter_list;
    def visitParameter(self, ctx:BKITParser.ParameterContext):
        return ctx.parameter_list().accept(self)

    # parameter_list: variable COMMA parameter_list | variable;
    def visitParameter_list(self, ctx:BKITParser.Parameter_listContext):
        var, dimen = ctx.variable().accept(self)
        init = []
        if ctx.parameter_list():
            return [VarDecl(var, dimen, init)] + ctx.parameter_list().accept(self)
        else:
            return [VarDecl(var, dimen, init)]

    # body: BODY COLON stmt_list ENDBODY DOT;
    def visitBody(self, ctx:BKITParser.BodyContext):
        varDecl, stmt = ctx.stmt_list().accept(self)
        return [varDecl, stmt]

    # var_list: variable_decl var_list | variable_decl;
    def visitVar_list(self, ctx:BKITParser.Var_listContext):
        if ctx.getChildCount() == 1:
            return [x for x in ctx.variable_decl().accept(self)]
        else:
            return [x for x in ctx.variable_decl().accept(self)] + ctx.var_list().accept(self)

    # stmt: assign_stmt | if_stmt | for_stmt | while_stmt | do_while_stmt | break_stmt | continue_stmt | call_stmt | return_stmt;
    def visitStmt(self, ctx:BKITParser.StmtContext):
        if ctx.assign_stmt():
            return ctx.assign_stmt().accept(self)
        elif ctx.if_stmt():
            return ctx.if_stmt().accept(self)
        elif ctx.for_stmt():
            return ctx.for_stmt().accept(self)
        elif ctx.while_stmt():
            return ctx.while_stmt().accept(self)
        elif ctx.do_while_stmt():
            return ctx.do_while_stmt().accept(self)
        elif ctx.break_stmt():
            return ctx.break_stmt().accept(self)
        elif ctx.continue_stmt():
            return ctx.continue_stmt().accept(self)
        elif ctx.call_stmt():
            return ctx.call_stmt().accept(self)
        elif ctx.return_stmt():
            return ctx.return_stmt().accept(self)

    # stmt_list: var_list? stmt*;
    def visitStmt_list(self, ctx:BKITParser.Stmt_listContext):
        varList = ctx.var_list().accept(self) if ctx.var_list() else []
        stmtList = []
        for i in range(len(ctx.stmt())):
            stmtList += [ctx.stmt(i).accept(self)]
        return (varList, stmtList)
    # # assign_stmt: ID index_operators? ASSIGN exp SEMI;
    # def visitAssign_stmt(self, ctx:BKITParser.Assign_stmtContext):
    #     return Assign(ArrayCell(Id(ctx.ID().getText()),ctx.index_operators().accept(self)),ctx.exp().accept(self)) if ctx.index_operators() else Assign(Id(ctx.ID().getText()),ctx.exp().accept(self))

    # assign_stmt: exp6 ASSIGN exp SEMI;
    def visitAssign_stmt(self, ctx:BKITParser.Assign_stmtContext):
        return Assign(ctx.exp6().accept(self),ctx.exp().accept(self))

    # if_stmt: IF exp THEN stmt_list else_if? (ELSE stmt_list)? ENDIF DOT;
    def visitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        exprIf = ctx.exp().accept(self)
        varDeclIf, stmtIf = ctx.stmt_list(0).accept(self)
        ifthenStmt = [(exprIf, varDeclIf, stmtIf)]

        ifthenStmt += ctx.else_if().accept(self) if ctx.else_if() else []

        elseStmt = ctx.stmt_list(1).accept(self) if ctx.ELSE() else ([],[])
        return If(ifthenStmt, elseStmt)

    # else_if: ELSEIF exp THEN stmt_list else_if | ELSEIF exp THEN stmt_list;
    def visitElse_if(self, ctx:BKITParser.Else_ifContext):
        expr = ctx.exp().accept(self)
        varDecl, stmt = ctx.stmt_list().accept(self)
        return [(expr, varDecl, stmt)] + ctx.else_if().accept(self) if ctx.else_if() else [(expr, varDecl, stmt)]

    # for_stmt: FOR LEFT_PAREN for_condition RIGHT_PAREN DO stmt_list ENDFOR DOT;
    def visitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        idx1, expr1, expr2, expr3 = ctx.for_condition().accept(self)
        varDecl, stmt = ctx.stmt_list().accept(self)
        loop = (varDecl, stmt)
        return For(idx1, expr1, expr2, expr3, loop)

    # for_condition: ID ASSIGN exp COMMA exp COMMA exp;
    def visitFor_condition(self, ctx:BKITParser.For_conditionContext):
        idx1 = Id(ctx.ID().getText())
        expr1 = ctx.exp(0).accept(self)
        expr2 = ctx.exp(1).accept(self)
        expr3 = ctx.exp(2).accept(self)
        return (idx1, expr1, expr2, expr3)

    # while_stmt: WHILE exp DO stmt_list ENDWHILE DOT;
    def visitWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        expr = ctx.exp().accept(self)
        varDecl, stmt = ctx.stmt_list().accept(self)
        loop = (varDecl, stmt)
        return While(expr, loop)

    # do_while_stmt: DO stmt_list WHILE exp ENDDO DOT;
    def visitDo_while_stmt(self, ctx:BKITParser.Do_while_stmtContext):
        expr = ctx.exp().accept(self)
        varDecl, stmt = ctx.stmt_list().accept(self)
        loop = (varDecl, stmt)
        return Dowhile(loop, expr)

    # break_stmt: BREAK SEMI;
    def visitBreak_stmt(self, ctx:BKITParser.Break_stmtContext):
        return Break()

    # continue_stmt: CONTINUE SEMI;
    def visitContinue_stmt(self, ctx:BKITParser.Continue_stmtContext):
        return Continue()

    # call_stmt: ID LEFT_PAREN exp_list? RIGHT_PAREN SEMI;
    def visitCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        method = Id(ctx.ID().getText())
        param = ctx.exp_list().accept(self) if ctx.exp_list() else []
        return CallStmt(method, param)

    # return_stmt: RETURN exp? SEMI;
    def visitReturn_stmt(self, ctx:BKITParser.Return_stmtContext):
        return Return(ctx.exp().accept(self) if ctx.exp() else None)

    # function_call: ID LEFT_PAREN exp_list? RIGHT_PAREN;
    def visitFunction_call(self, ctx:BKITParser.Function_callContext):
        method = Id(ctx.ID().getText())
        param = ctx.exp_list().accept(self) if ctx.exp_list() else []
        return CallExpr(method, param)

    # exp: exp1 relational_operators exp1 | exp1;
    def visitExp(self, ctx:BKITParser.ExpContext):
        return BinaryOp(ctx.relational_operators().getText(),ctx.exp1(0).accept(self),ctx.exp1(1).accept(self)) if ctx.relational_operators() else ctx.exp1(0).accept(self)

    # exp1: exp1 boolean_operators exp2 | exp2;
    def visitExp1(self, ctx:BKITParser.Exp1Context):
        return BinaryOp(ctx.boolean_operators().getText(),ctx.exp1().accept(self),ctx.exp2().accept(self)) if ctx.boolean_operators() else ctx.exp2().accept(self)

    # exp2: exp2 adding_operators exp3 | exp3;
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        return BinaryOp(ctx.adding_operators().getText(),ctx.exp2().accept(self),ctx.exp3().accept(self)) if ctx.adding_operators() else ctx.exp3().accept(self)

    # exp3: exp3 multiplying_operators exp4 | exp4;
    def visitExp3(self, ctx:BKITParser.Exp3Context):
        return BinaryOp(ctx.multiplying_operators().getText(),ctx.exp3().accept(self),ctx.exp4().accept(self)) if ctx.multiplying_operators() else ctx.exp4().accept(self)

    # exp4: NOT exp4 | exp5;
    def visitExp4(self, ctx:BKITParser.Exp4Context):
        return UnaryOp(ctx.NOT().getText(),ctx.exp4().accept(self)) if ctx.NOT() else ctx.exp5().accept(self)

    # exp5: sign_operators exp5 | exp6;
    def visitExp5(self, ctx:BKITParser.Exp5Context):
        return UnaryOp(ctx.sign_operators().getText(),ctx.exp5().accept(self)) if ctx.sign_operators() else ctx.exp6().accept(self)

    # exp6: exp6 index_operators | exp7;
    def visitExp6(self, ctx:BKITParser.Exp6Context):
        return ArrayCell(ctx.exp6().accept(self),ctx.index_operators().accept(self)) if ctx.index_operators() else ctx.exp7().accept(self)

    # exp7: function_call | LEFT_PAREN exp RIGHT_PAREN | operands;
    def visitExp7(self, ctx:BKITParser.Exp7Context):
        if ctx.getChildCount() > 1:
            return ctx.exp().accept(self)
        else:
            return ctx.function_call().accept(self) if ctx.function_call() else ctx.operands().accept(self)

    # exp_list: exp COMMA exp_list | exp;
    def visitExp_list(self, ctx:BKITParser.Exp_listContext):
        return [ctx.exp().accept(self)] + ctx.exp_list().accept(self) if ctx.exp_list() else [ctx.exp().accept(self)]

    # # operands: ID | literal | element_exp;
    # def visitOperands(self, ctx:BKITParser.OperandsContext):
    #     if ctx.ID():
    #         return Id(ctx.ID().getText())
    #     elif ctx.literal():
    #         return ctx.literal().accept(self)
    #     else:
    #         return ctx.element_exp().accept(self)

    # operands: ID | literal;
    def visitOperands(self, ctx:BKITParser.OperandsContext):
        return Id(ctx.ID().getText()) if ctx.ID() else ctx.literal().accept(self)

    # multiplying_operators: MULTI | MULTI_F | DIV | DIV_F | MOD;
    def visitMultiplying_operators(self, ctx:BKITParser.Multiplying_operatorsContext):
        return ctx.getText()

    # adding_operators: ADD | ADD_F | SUB | SUB_F;
    def visitAdding_operators(self, ctx:BKITParser.Adding_operatorsContext):
        return ctx.getText()

    # sign_operators: SUB| SUB_F;
    def visitSign_operators(self, ctx:BKITParser.Sign_operatorsContext):
        return ctx.getText()

    # boolean_operators: ANDAND | OROR;
    def visitBoolean_operators(self, ctx:BKITParser.Boolean_operatorsContext):
        return ctx.getText()

    # relational_operators: EQUAL | NOT_EQUAL | LESS_THAN | GREATER_THAN | GREATER_EQUAL | LESS_EQUAL | NOT_EQUAL_F | LESS_THAN_F | GREATER_THAN_F | GREATER_EQUAL_F | LESS_EQUAL_F;
    def visitRelational_operators(self, ctx:BKITParser.Relational_operatorsContext):
        print(ctx.getText())
        return ctx.getText()

    # element_exp: expr_index index_operators;
    def visitElement_exp(self, ctx:BKITParser.Element_expContext):
        return ctx.expr_index().accept(self) + ctx.index_operators().accept(self)

    # index_operators: LEFT_BRACKET exp RIGHT_BRACKET index_operators | LEFT_BRACKET exp RIGHT_BRACKET;
    def visitIndex_operators(self, ctx:BKITParser.Index_operatorsContext):
        return [ctx.exp().accept(self)] + ctx.index_operators().accept(self)  if ctx.index_operators() else [ctx.exp().accept(self)]

    # expr_index: ID | function_call;
    def visitExpr_index(self, ctx:BKITParser.Expr_indexContext):
        return Id(ctx.ID().getText()) if ctx.ID() else ctx.function_call().accept(self)

