from LinearRegression import LinearRegression
import pandas as pd

def main():
    file = 'benetton.csv'
    df = pd.read_csv(file)
    x_name = 'Advertising'
    y_name = 'Sales'
    x_train = df[x_name].tolist()
    y_train = df[y_name].tolist()
    
    model = LinearRegression(x_train, y_train)
    
    # Compute the coefficients of the linear equation
    beta0, beta1 = model.fit()
    
    # Predict Y for given X
    y_predict = model.predict(x_train)
    
    # Correlation and determination coefficients
    correlation_coeff, determination_coeff = model.correlationCoefficient()
    
    print(f"""
    -----------------------------------------
    -----------------------------------------
    LINEAR REGRESSION EQUATION ( y = a + bx ):
    -----------------------------------------
    
    {y_name} = {beta0} + {beta1} {x_name}
    
    ----------------------------------------
    Given X predict Y:
    ----------------------------------------
    
    Original {x_name} (X values):
    {x_train}
    
    Expected {y_name} (original Y values):
    {y_train}
    
    Predicted {y_name} (predicted Y values):
    {y_predict}

    ----------------------------------------
    Correlation and determination coefficients: 
    ----------------------------------------
    
    Correlation coefficient: {correlation_coeff}
    
    Determination coefficient: {determination_coeff}

    
    """)
    

if __name__ == "__main__":
    main()