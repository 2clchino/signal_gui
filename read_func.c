#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdint.h>

int64_t* value(void);
int64_t buf[32];

int main(void){
  int64_t* buf=value();
  for (int i=0; i<32; i++)
    printf("%02x: %016lx\n", i, buf[i]);
}

int64_t* value(void){
  int fd = open("/dev/xdma0_c2h_0", O_RDONLY);
  printf("FD: %d\n", fd);
  
  unsigned int pos = lseek(fd, 0xc0000000, SEEK_SET); // BRAM
  printf("%x\n", pos);
  
  int len = read(fd, buf, 32*8);
  close(fd);
  printf("Len: %d\n", len);
  return buf;
}