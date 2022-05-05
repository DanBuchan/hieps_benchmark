library(ggplot2)

identity_data <- read.csv("/home/dbuchan/Projects/hieps/data/identity_performance.csv", header=T)
eval_data <- read.csv("/home/dbuchan/Projects/hieps/data/evalue_performance.csv", header=T)

ggplot(data=eval_data, aes(x=evalue, y=average_sensitivity)) + geom_line() + geom_point()
ggsave("/home/dbuchan/Projects/hieps/data/eval_sensitivity.png", dpi=100, width=800, height=600, units="px")

ggplot(data=eval_data, aes(x=evalue, y=average_precision)) + geom_line() + geom_point()
ggsave("/home/dbuchan/Projects/hieps/data/eval_precision.png", dpi=100, width=800, height=600, units="px")

ggplot(data=identity_data, aes(x=percentage_identity, y=average_sensitivity)) + geom_line() + geom_point()
ggsave("/home/dbuchan/Projects/hieps/data/identity_sensitvity.png", dpi=100, width=800, height=600, units="px")

ggplot(data=identity_data, aes(x=percentage_identity, y=average_precision)) + geom_line() + geom_point()
ggsave("/home/dbuchan/Projects/hieps/data/identity_precision.png", dpi=100, width=800, height=600, units="px")
