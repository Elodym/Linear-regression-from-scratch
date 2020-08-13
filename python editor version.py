def linearreg():
    x = [1,2,3]
    y = [4,5,6]
    df = pd.DataFrame({'x':x,'y':y})
    df['xy'] = df['x']*df['y']
    df['x2'] = df['x']**2
    b = (df['xy'].sum()-df['x'].sum()*df['y'].sum()/len(x))/(df['x2'].sum()-df['x'].sum()**2/len(x))
    a = df['y'].sum()/len(x)-b*df['x'].sum()/len(x)
    df['^y'] = a + b*df['x']
    print('Fitted regression: y = '+str(a)+' + '+str(b)+'x')
    plt.scatter(df['x'], df['y'])
    plt.plot(df['x'], df['^y'], color='orange')
