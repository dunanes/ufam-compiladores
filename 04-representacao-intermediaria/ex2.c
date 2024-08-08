int count;
int loop(int max) {
  int i;
  i = 0;
  while (i < max) {
    i++;
    if (i == max) {
      break;
    }
  }
  return i;
}
