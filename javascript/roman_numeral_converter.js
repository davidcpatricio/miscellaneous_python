function convertToRoman(num) {
    if (num > 3999 || num < 1 || ! Number.isInteger(num)) {
      return "Can't convert to roman";
    }
  
    const decimalNumerals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    const romanNumerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
  
    let roman = "";
  
    for (let i = 0; i < decimalNumerals.length; i++) {
      while (num >= decimalNumerals[i]) {
        roman += romanNumerals[i]
        num -= decimalNumerals[i]
      }
    }
  
    return roman;
}
