export const test = (
  { handler, result }: { result: number; handler: (...rest: any[]) => any },
  ...rest: any[]
) => {
  //@ts-ignore
  const res = handler(...rest);
  if (res !== result) {
    console.error("failed expected: " + result + " but recived " + res);
  } else {
    console.log("Passed");
  }
};
