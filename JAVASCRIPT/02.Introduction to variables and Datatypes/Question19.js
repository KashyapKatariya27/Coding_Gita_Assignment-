const numberValue = Number.MAX_SAFE_INTEGER;
const bigIntValue = BigInt(numberValue);

for (const increment of [1, 2, 3]) {
  const result = numberValue + increment;
  console.log(`Number + ${increment}:`, result, typeof result);
}

for (const increment of [1n, 2n, 3n]) {
  const result = bigIntValue + increment;
  console.log(`BigInt + ${increment}:`, result, typeof result);
}