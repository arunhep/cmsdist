### RPM external mctester-toolfile 1.0
Requires: mctester
%prep

%build

%install

mkdir -p %i/etc/scram.d
cat << \EOF_TOOLFILE >%i/etc/scram.d/mctester.xml
<tool name="mctester" version="@TOOL_VERSION@">
  <lib name="HEPEvent"/>
  <lib name="HepMCEvent"/>
  <lib name="MCTester"/>
  <client>
    <environment name="MC_TESTER_BASE" default="@TOOL_ROOT@"/>
    <environment name="LIBDIR" default="$MC_TESTER_BASE/lib"/>
    <environment name="INCLUDE" default="$MC_TESTER_BASE/include"/>
  </client>
  <use name="root"/>
  <use name="HepMC"/>
  <use name="pythia8"/>
</tool>
EOF_TOOLFILE

## IMPORT scram-tools-post

