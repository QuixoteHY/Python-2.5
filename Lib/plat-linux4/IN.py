# Generated by h2py from /usr/include/netinet/in.h
_NETINET_IN_H = 1

# Included from features.h
_FEATURES_H = 1
_DEFAULT_SOURCE = 1
_ISOC95_SOURCE = 1
_ISOC99_SOURCE = 1
_ISOC11_SOURCE = 1
_POSIX_SOURCE = 1
_POSIX_C_SOURCE = 200809L
_XOPEN_SOURCE = 700
_XOPEN_SOURCE_EXTENDED = 1
_LARGEFILE64_SOURCE = 1
_DEFAULT_SOURCE = 1
_ATFILE_SOURCE = 1
_DEFAULT_SOURCE = 1
__USE_ISOC11 = 1
__USE_ISOC99 = 1
__USE_ISOC95 = 1
__USE_ISOCXX11 = 1
__USE_POSIX_IMPLICITLY = 1
_POSIX_SOURCE = 1
_POSIX_C_SOURCE = 200809L
_POSIX_SOURCE = 1
_POSIX_C_SOURCE = 2
_POSIX_C_SOURCE = 199506L
_POSIX_C_SOURCE = 200112L
_POSIX_C_SOURCE = 200809L
__USE_POSIX_IMPLICITLY = 1
__USE_POSIX = 1
__USE_POSIX2 = 1
__USE_POSIX199309 = 1
__USE_POSIX199506 = 1
__USE_XOPEN2K = 1
__USE_ISOC95 = 1
__USE_ISOC99 = 1
__USE_XOPEN2K8 = 1
_ATFILE_SOURCE = 1
__USE_XOPEN = 1
__USE_XOPEN_EXTENDED = 1
__USE_UNIX98 = 1
_LARGEFILE_SOURCE = 1
__USE_XOPEN2K8 = 1
__USE_XOPEN2K8XSI = 1
__USE_XOPEN2K = 1
__USE_XOPEN2KXSI = 1
__USE_ISOC95 = 1
__USE_ISOC99 = 1
__USE_XOPEN_EXTENDED = 1
__USE_LARGEFILE = 1
__USE_LARGEFILE64 = 1
__USE_FILE_OFFSET64 = 1
__USE_MISC = 1
__USE_ATFILE = 1
__USE_GNU = 1
__USE_REENTRANT = 1
__USE_FORTIFY_LEVEL = 2
__USE_FORTIFY_LEVEL = 1
__USE_FORTIFY_LEVEL = 0
__GNU_LIBRARY__ = 6
__GLIBC__ = 2
__GLIBC_MINOR__ = 23
__USE_LARGEFILE = 1
__USE_LARGEFILE64 = 1
__USE_EXTERN_INLINES = 1

# Included from stdint.h
_STDINT_H = 1
def __INT64_C(c): return c ## L

def __UINT64_C(c): return c ## UL

def __INT64_C(c): return c ## LL

def __UINT64_C(c): return c ## ULL

INT8_MIN = (-128)
INT16_MIN = (-32767-1)
INT32_MIN = (-2147483647-1)
INT64_MIN = (-__INT64_C(9223372036854775807)-1)
INT8_MAX = (127)
INT16_MAX = (32767)
INT32_MAX = (2147483647)
INT64_MAX = (__INT64_C(9223372036854775807))
UINT8_MAX = (255)
UINT16_MAX = (65535)
UINT64_MAX = (__UINT64_C(18446744073709551615))
INT_LEAST8_MIN = (-128)
INT_LEAST16_MIN = (-32767-1)
INT_LEAST32_MIN = (-2147483647-1)
INT_LEAST64_MIN = (-__INT64_C(9223372036854775807)-1)
INT_LEAST8_MAX = (127)
INT_LEAST16_MAX = (32767)
INT_LEAST32_MAX = (2147483647)
INT_LEAST64_MAX = (__INT64_C(9223372036854775807))
UINT_LEAST8_MAX = (255)
UINT_LEAST16_MAX = (65535)
UINT_LEAST64_MAX = (__UINT64_C(18446744073709551615))
INT_FAST8_MIN = (-128)
INT_FAST16_MIN = (-9223372036854775807L-1)
INT_FAST32_MIN = (-9223372036854775807L-1)
INT_FAST16_MIN = (-2147483647-1)
INT_FAST32_MIN = (-2147483647-1)
INT_FAST64_MIN = (-__INT64_C(9223372036854775807)-1)
INT_FAST8_MAX = (127)
INT_FAST16_MAX = (9223372036854775807L)
INT_FAST32_MAX = (9223372036854775807L)
INT_FAST16_MAX = (2147483647)
INT_FAST32_MAX = (2147483647)
INT_FAST64_MAX = (__INT64_C(9223372036854775807))
UINT_FAST8_MAX = (255)
UINT_FAST64_MAX = (__UINT64_C(18446744073709551615))
INTPTR_MIN = (-9223372036854775807L-1)
INTPTR_MAX = (9223372036854775807L)
INTPTR_MIN = (-2147483647-1)
INTPTR_MAX = (2147483647)
INTMAX_MIN = (-__INT64_C(9223372036854775807)-1)
INTMAX_MAX = (__INT64_C(9223372036854775807))
UINTMAX_MAX = (__UINT64_C(18446744073709551615))
PTRDIFF_MIN = (-9223372036854775807L-1)
PTRDIFF_MAX = (9223372036854775807L)
PTRDIFF_MIN = (-2147483647-1)
PTRDIFF_MAX = (2147483647)
SIG_ATOMIC_MIN = (-2147483647-1)
SIG_ATOMIC_MAX = (2147483647)
def INT8_C(c): return c

def INT16_C(c): return c

def INT32_C(c): return c

def INT64_C(c): return c ## L

def INT64_C(c): return c ## LL

def UINT8_C(c): return c

def UINT16_C(c): return c

def UINT32_C(c): return c ## U

def UINT64_C(c): return c ## UL

def UINT64_C(c): return c ## ULL

def INTMAX_C(c): return c ## L

def UINTMAX_C(c): return c ## UL

def INTMAX_C(c): return c ## LL

def UINTMAX_C(c): return c ## ULL

def IN_CLASSA(a): return ((((in_addr_t)(a)) & 0x80000000) == 0)

IN_CLASSA_NET = 0xff000000
IN_CLASSA_NSHIFT = 24
IN_CLASSA_HOST = (0xffffffff & ~IN_CLASSA_NET)
IN_CLASSA_MAX = 128
def IN_CLASSB(a): return ((((in_addr_t)(a)) & 0xc0000000) == 0x80000000)

IN_CLASSB_NET = 0xffff0000
IN_CLASSB_NSHIFT = 16
IN_CLASSB_HOST = (0xffffffff & ~IN_CLASSB_NET)
IN_CLASSB_MAX = 65536
def IN_CLASSC(a): return ((((in_addr_t)(a)) & 0xe0000000) == 0xc0000000)

IN_CLASSC_NET = 0xffffff00
IN_CLASSC_NSHIFT = 8
IN_CLASSC_HOST = (0xffffffff & ~IN_CLASSC_NET)
def IN_CLASSD(a): return ((((in_addr_t)(a)) & 0xf0000000) == 0xe0000000)

def IN_MULTICAST(a): return IN_CLASSD(a)

def IN_EXPERIMENTAL(a): return ((((in_addr_t)(a)) & 0xe0000000) == 0xe0000000)

def IN_BADCLASS(a): return ((((in_addr_t)(a)) & 0xf0000000) == 0xf0000000)

IN_LOOPBACKNET = 127
INET_ADDRSTRLEN = 16
INET6_ADDRSTRLEN = 46

# Included from endian.h
_ENDIAN_H = 1
__LITTLE_ENDIAN = 1234
__BIG_ENDIAN = 4321
__PDP_ENDIAN = 3412
LITTLE_ENDIAN = __LITTLE_ENDIAN
BIG_ENDIAN = __BIG_ENDIAN
PDP_ENDIAN = __PDP_ENDIAN
def htobe16(x): return __bswap_16 (x)

def htole16(x): return (x)

def be16toh(x): return __bswap_16 (x)

def le16toh(x): return (x)

def htobe32(x): return __bswap_32 (x)

def htole32(x): return (x)

def be32toh(x): return __bswap_32 (x)

def le32toh(x): return (x)

def htobe64(x): return __bswap_64 (x)

def htole64(x): return (x)

def be64toh(x): return __bswap_64 (x)

def le64toh(x): return (x)

def htobe16(x): return (x)

def htole16(x): return __bswap_16 (x)

def be16toh(x): return (x)

def le16toh(x): return __bswap_16 (x)

def htobe32(x): return (x)

def htole32(x): return __bswap_32 (x)

def be32toh(x): return (x)

def le32toh(x): return __bswap_32 (x)

def htobe64(x): return (x)

def htole64(x): return __bswap_64 (x)

def be64toh(x): return (x)

def le64toh(x): return __bswap_64 (x)

def ntohl(x): return (x)

def ntohs(x): return (x)

def htonl(x): return (x)

def htons(x): return (x)

def ntohl(x): return __bswap_32 (x)

def ntohs(x): return __bswap_16 (x)

def htonl(x): return __bswap_32 (x)

def htons(x): return __bswap_16 (x)

def IN6_IS_ADDR_UNSPECIFIED(a): return \

def IN6_IS_ADDR_LOOPBACK(a): return \

def IN6_IS_ADDR_LINKLOCAL(a): return \

def IN6_IS_ADDR_SITELOCAL(a): return \

def IN6_IS_ADDR_V4MAPPED(a): return \

def IN6_IS_ADDR_V4COMPAT(a): return \

def IN6_IS_ADDR_UNSPECIFIED(a): return \

def IN6_IS_ADDR_LOOPBACK(a): return \

def IN6_IS_ADDR_LINKLOCAL(a): return \

def IN6_IS_ADDR_SITELOCAL(a): return \

def IN6_IS_ADDR_V4MAPPED(a): return \

def IN6_IS_ADDR_V4COMPAT(a): return \

def IN6_IS_ADDR_MC_NODELOCAL(a): return \

def IN6_IS_ADDR_MC_LINKLOCAL(a): return \

def IN6_IS_ADDR_MC_SITELOCAL(a): return \

def IN6_IS_ADDR_MC_ORGLOCAL(a): return \

def IN6_IS_ADDR_MC_GLOBAL(a): return \

