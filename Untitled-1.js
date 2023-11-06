const maxIterations = Math.pow(2, 32);//4.294.967.296

const fluctuations = (fluctuation) => Array.from({ length: 12 }, () => Math.random() * (fluctuation * 2) - fluctuation); 

function externalFactor(randomNumbers, prob) {
    for (let i = 0; i < randomNumbers.length; i++)
        if (Math.random() <= prob) {
            // Reemplazo un número al azar de la lista por un valor entre -100 y 100
            const randomIndex = Math.floor(Math.random() * 12);
            randomNumbers[randomIndex] = Math.random() * 200 - 100;
        } 
}

function annualEfficiency(expectedEff, error, fluctuation, externalProb) {
    for (let i = 0; i < maxIterations; i++) {
        const randomNumbers = fluctuations(fluctuation);
        const sum = randomNumbers.reduce((acc, val) => acc + val, 0);
        if (Math.abs(sum - expectedEff) <= error) {
            externalFactor(randomNumbers, externalProb);
            console.log(i);
            return randomNumbers;
        }
    }
    throw new Error(`No se encontró una solución válida después de ${maxIterations} iteraciones.`);
}

function calculateProfit(initialValue, expectedEff, error, fluctuation, externalProb) {
    const monthlyPercents = annualEfficiency(expectedEff, error, fluctuation, externalProb);
    const monthlyProfit = []; 

    for (let i = 0; i < monthlyPercents.length; i++){ 
        if(i === 0)
            monthlyProfit.push(initialValue + initialValue * (monthlyPercents[i] / 100));
        else
            monthlyProfit.push(monthlyProfit[i - 1] + monthlyProfit[i - 1] * (monthlyPercents[i]/100));
    }
    return {monthlyProfit, monthlyPercents};
}

const expecteEff = 10; //100% de rendimiento 
const allowError = 0.1; //Se permite allowError >= expecteEff/100
const fluctuation = 1;//0.01; //Representa la estabilidad de la inversion. x < flutctuation < expectedEff/10
const factor = 0.01; //Hay un 1% de probabilidades de ue se genere un movimiento no planeado o externo
const initialValue = 1500; 

generated = calculateProfit(initialValue, expecteEff, allowError, fluctuation, factor);
console.log(generated); 
const percents = generated.monthlyPercents.reduce((a, b) => a + b, 0); 
console.log(initialValue*percents/100, percents);