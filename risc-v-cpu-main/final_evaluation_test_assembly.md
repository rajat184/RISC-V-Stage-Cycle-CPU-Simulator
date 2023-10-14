<hr>

## <B>Assembly Code</B>

<table width=100%>
<tr>
<td>

```
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
```

</td>
<td width=100%>

```
ADDI    r31     r0      6
ADDI    r30     r0      2
ADDI    r2      r0      1
SW      r1      r3      0
SW      r2      r3      4
ADDI    r3      r3      4
ADD     r4      r1      r2
ADD     r1      r0      r2
ADD     r2      r0      r4
SW      r4      r3      4
ADDI    r30     r30     1
BEQ     r30     r31     8
BEQ     r0      r0      -28
LW      r11     r0      12
SUB     r13     r11     r3
LW      r12     r0      8
SLL     r21     r11     r13
SRA     r14     r21     r12
AND     r15     r21     r14
OR      r16     r21     r14
LOADNOC r16     r14     4
STORENOC

```

</td>
</tr>
</table>

<br>
<hr>
