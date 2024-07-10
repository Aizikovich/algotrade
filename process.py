import matplotlib.pyplot as plt
import pandas as pd


def change_names(df):
    # change all name to lowers and replace spaces with underscores
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    return df


def add_mean(df):
    # add mean column to the dataframe
    df['mean'] = df[['High', 'Low']].mean(axis=1)
    return df


def add_up_and_down_stds(df):
    std = df['mean'].std()
    df['up_std'] = df['mean'] + std
    df['down_std'] = df['mean'] - std
    return df


def plot_data(df, columns):
    # plot the data
    for col in columns:
        plt.plot(df[col], label=col)
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Stock Prices')
    plt.show()


if __name__ == '__main__':
    voo = pd.read_csv('data/yfdata/VOO.csv')
    voo = add_mean(voo)
    voo = add_up_and_down_stds(voo)
    print(voo.head())
    plot_data(voo, columns=['mean', 'up_std', 'down_std'])
