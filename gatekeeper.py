class ArchDecision:
    def __init__(self):
        self.SLOTS = {
            "MO": "MODULE_ISOLATION -> single_responsibility_enforced",
            "DT": "DATA_TOPOLOGY   -> dict_centralized, no_scatter",
            "FL": "FLOW_LOCK       -> linear_loop, no_nested_branch",
            "EP": "ENTRY_POINT     -> __main__ only, no_scaffold"
        }

    def run(self):
        print("\n=== ArchDecision: Pre-commit Gate ===")
        while True:
            try:
                key = input("\n[ARCH_CHECK] >> ").strip().upper()
                if len(key) < 2: continue
                print(f"DECISION: {self.SLOTS.get(key[:2], 'LOGIC_CONFLICT -> REJECT')}")
            except EOFError: break

if __name__ == "__main__":
    ArchDecision().run()
