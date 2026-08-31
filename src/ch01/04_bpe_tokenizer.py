class BPETokenizer:
    def __init__(self, merge_rules):
        self.merge_rules = merge_rules

        self.id_to_bytes = {i: bytes([i]) for i in range(256)}

        for (id1, id2), new_id in merge_rules.items():
            self.id_to_bytes[new_id] = self.id_to_bytes[id1] + self.id_to_bytes[id2]

        self.vocab_size = len(self.id_to_bytes)
