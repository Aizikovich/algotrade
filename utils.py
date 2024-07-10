from torch.utils.data import Dataset


class EtfDataset(Dataset):
    def __init__(self, data, window_size):
        self.data = data
        self.ws = window_size

    def __len__(self):
        pass

    def add_window(self):
        idxs = []
        for idx in range(0, len(self.data)-self.ws, self.ws):
            idxs.append(idx)
        print(idxs)


    def __getitem__(self, idx):
        pass

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    etf = EtfDataset(data, 3)
    etf.add_window()
