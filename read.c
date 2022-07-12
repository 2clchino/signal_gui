#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdint.h>

int main(){
  int fd = open("/dev/xdma0_c2h_0", O_RDONLY);
  printf("FD: %d\n", fd);
  
  unsigned int pos = lseek(fd, 0xc0000000, SEEK_SET); // BRAM

  printf("%x\n", pos);
  
  int64_t buf[32];
  int len = read(fd, buf, 32*8);
  close(fd);

  printf("Len: %d\n", len);
  
  for (int i=0; i<32; i++)
    printf("%02x: %016llx\n", i, buf[i]);
    
}
