grammar LTL;

options {
	tokenVocab = LTLLexer;
}

formula:
	NEGATION formula				# NegationFormula
	| formula CONJUNCTION formula	# ConjunctionFormula
	| formula DISJUNCTION formula	# DisjunctionFormula
	| formula IMPLICATION formula	# ImplicationFormula
	| NEXT formula					# NextFormula
	| ALWAYS formula				# AlwaysFormula
	| EVENTUALLY formula			# EventuallyFormula
	| formula UNTIL formula			# UntilFormula
	| LPAREN formula RPAREN			# ParenthesisFormula
	| atomic						# AtomicFormula;

atomic:
	IDENTIFIER                      # Identifier
	| TRUE                          # AtomicTrue
	| FALSE                         # AtomicFalse;
