#ifndef LFORTRAN_SEMANTICS_ASR_SCOPES_H
#define LFORTRAN_SEMANTICS_ASR_SCOPES_H

#include <map>

namespace LFortran  {

namespace ASR {
    struct asr_t;
}

struct SymbolTable {
    std::map<std::string, ASR::asr_t*> scope;
};

const int intent_local=0; // local variable (not a dummy argument)
const int intent_in   =1; // dummy argument, intent(in)
const int intent_out  =2; // dummy argument, intent(out)
const int intent_inout=3; // dummy argument, intent(inout)


struct SubroutineSymbol
{
    char* name;
    int type; // 1 = real, 2 = integer
    int intent; // 0 = local variable, >0 dummy: 1 = in, 2 = out, 3 = inout
};

} // namespace LFortran

#endif // LFORTRAN_SEMANTICS_ASR_SCOPES_H
