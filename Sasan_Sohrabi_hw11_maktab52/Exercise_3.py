# Exercise 3

# Import relevant libraries
import psycopg2

# Connect to an existing database
connection = psycopg2.connect(user="sasan.sp92",
                              password="09125915669",
                              host="127.0.0.1",
                              port="5432",
                              database="medical_laboratory")


# Open a cursor to perform database operations
cur = connection.cursor()


# Create tables

# 1- Create dispatcher table
cur.execute("CREATE TABLE public.dispatcher (dispatcher_id  SERIAL PRIMARY KEY, dispatcher_name VARCHAR(500) NOT NULL,"
            "dispatcher_phone VARCHAR(500) NOT NULL);")

# 2- Create patient table
cur.execute("CREATE TABLE public.patient (patient_id SERIAL PRIMARY KEY, first_name character(1) NOT NULL,"
            " last_name character(1) NOT NULL, national_code character(1) NOT NULL, birth_day date NOT NULL,"
            " phone character(1) NOT NULL, email character(1), password character(1), dispatcher_fk integer NOT NULL,"
            "FOREIGN KEY (dispatcher_fk) REFERENCES dispatcher(dispatcher_id) ON DELETE CASCADE);")


# Insert data in patient table
cur.execute("INSERT INTO public.dispatcher (dispatcher_name, dispatcher_phone) VALUES ("
            "'Tehrani', '+989124567890');")

connection.commit()

connection.close()



#
# --
# -- Name: dispatcher_dispatcher_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sasan.sp92
# --
#
# ALTER SEQUENCE public.dispatcher_dispatcher_id_seq OWNED BY public.dispatcher.dispatcher_id;
#
#
# --
# -- Name: employee; Type: TABLE; Schema: public; Owner: sasan.sp92
# --
#
# CREATE TABLE public.employee (
#     employee_id integer NOT NULL,
#     employee_first_name character(1) NOT NULL,
#     employee_last_name character(1) NOT NULL,
#     employee_phone character(1) NOT NULL,
#     employee_email character(1),
#     employee_address character(1) NOT NULL,
#     employee_quantification character(1) NOT NULL,
#     employee_work_period character(1) NOT NULL,
#     job_fk integer NOT NULL
# );
#
#
# ALTER TABLE public.employee OWNER TO "sasan.sp92";
#
# --
# -- Name: employee_employee_id_seq; Type: SEQUENCE; Schema: public; Owner: sasan.sp92
# --
#
# CREATE SEQUENCE public.employee_employee_id_seq
#     AS integer
#     START WITH 1
#     INCREMENT BY 1
#     NO MINVALUE
#     NO MAXVALUE
#     CACHE 1;
#
#
# ALTER TABLE public.employee_employee_id_seq OWNER TO "sasan.sp92";
#
# --
# -- Name: employee_employee_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sasan.sp92
# --
#
# ALTER SEQUENCE public.employee_employee_id_seq OWNED BY public.employee.employee_id;
#
#
# --
# -- Name: job; Type: TABLE; Schema: public; Owner: sasan.sp92
# --
#
# CREATE TABLE public.job (
#     job_id integer NOT NULL,
#     job_name character(1) NOT NULL,
#     job_description character(1) NOT NULL
# );
#
#
# ALTER TABLE public.job OWNER TO "sasan.sp92";
#
# --
# -- Name: job_job_id_seq; Type: SEQUENCE; Schema: public; Owner: sasan.sp92
# --
#
# CREATE SEQUENCE public.job_job_id_seq
#     AS integer
#     START WITH 1
#     INCREMENT BY 1
#     NO MINVALUE
#     NO MAXVALUE
#     CACHE 1;
#
#
# ALTER TABLE public.job_job_id_seq OWNER TO "sasan.sp92";
#
# --
# -- Name: job_job_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sasan.sp92
# --
#
# ALTER SEQUENCE public.job_job_id_seq OWNED BY public.job.job_id;
#
#
# --
# -- Name: patient; Type: TABLE; Schema: public; Owner: sasan.sp92
# --
#
# CREATE TABLE public.patient (
#     patient_id integer NOT NULL,
#     first_name character(1) NOT NULL,
#     last_name character(1) NOT NULL,
#     national_code character(1) NOT NULL,
#     birth_day date NOT NULL,
#     phone character(1) NOT NULL,
#     email character(1),
#     password character(1),
#     dispatcher_fk integer NOT NULL
# );
#
#
# ALTER TABLE public.patient OWNER TO "sasan.sp92";
#
# --
# -- Name: patient_patient_id_seq; Type: SEQUENCE; Schema: public; Owner: sasan.sp92
# --
#
# CREATE SEQUENCE public.patient_patient_id_seq
#     AS integer
#     START WITH 1
#     INCREMENT BY 1
#     NO MINVALUE
#     NO MAXVALUE
#     CACHE 1;
#
#
# ALTER TABLE public.patient_patient_id_seq OWNER TO "sasan.sp92";
#
# --
# -- Name: patient_patient_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sasan.sp92
# --
#
# ALTER SEQUENCE public.patient_patient_id_seq OWNED BY public.patient.patient_id;
#
#
# --
# -- Name: payment; Type: TABLE; Schema: public; Owner: sasan.sp92
# --
#
# CREATE TABLE public.payment (
#     payment_id integer NOT NULL,
#     patient_fk integer NOT NULL,
#     test_fk integer NOT NULL,
#     payment_amount integer NOT NULL,
#     payment_date date NOT NULL
# );
#
#
# ALTER TABLE public.payment OWNER TO "sasan.sp92";
#
# --
# -- Name: payment_payment_id_seq; Type: SEQUENCE; Schema: public; Owner: sasan.sp92
# --
#
# CREATE SEQUENCE public.payment_payment_id_seq
#     AS integer
#     START WITH 1
#     INCREMENT BY 1
#     NO MINVALUE
#     NO MAXVALUE
#     CACHE 1;
#
#
# ALTER TABLE public.payment_payment_id_seq OWNER TO "sasan.sp92";
#
# --
# -- Name: payment_payment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sasan.sp92
# --
#
# ALTER SEQUENCE public.payment_payment_id_seq OWNED BY public.payment.payment_id;
#
#
# --
# -- Name: result; Type: TABLE; Schema: public; Owner: sasan.sp92
# --
#
# CREATE TABLE public.result (
#     result_id integer NOT NULL,
#     patient_fk integer NOT NULL,
#     sample_fk integer NOT NULL,
#     employee_fk integer NOT NULL,
#     test_fk integer NOT NULL,
#     result_value character(1) NOT NULL
# );
#
#
# ALTER TABLE public.result OWNER TO "sasan.sp92";
#
# --
# -- Name: result_result_id_seq; Type: SEQUENCE; Schema: public; Owner: sasan.sp92
# --
#
# CREATE SEQUENCE public.result_result_id_seq
#     AS integer
#     START WITH 1
#     INCREMENT BY 1
#     NO MINVALUE
#     NO MAXVALUE
#     CACHE 1;
#
#
# ALTER TABLE public.result_result_id_seq OWNER TO "sasan.sp92";
#
# --
# -- Name: result_result_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sasan.sp92
# --
#
# ALTER SEQUENCE public.result_result_id_seq OWNED BY public.result.result_id;
#
#
# --
# -- Name: sample; Type: TABLE; Schema: public; Owner: sasan.sp92
# --
#
# CREATE TABLE public.sample (
#     sample_id integer NOT NULL,
#     patient_fk integer NOT NULL,
#     sample_type_fk integer NOT NULL
# );
#
#
# ALTER TABLE public.sample OWNER TO "sasan.sp92";
#
# --
# -- Name: sample_sample_id_seq; Type: SEQUENCE; Schema: public; Owner: sasan.sp92
# --
#
# CREATE SEQUENCE public.sample_sample_id_seq
#     AS integer
#     START WITH 1
#     INCREMENT BY 1
#     NO MINVALUE
#     NO MAXVALUE
#     CACHE 1;
#
#
# ALTER TABLE public.sample_sample_id_seq OWNER TO "sasan.sp92";
#
# --
# -- Name: sample_sample_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sasan.sp92
# --
#
# ALTER SEQUENCE public.sample_sample_id_seq OWNED BY public.sample.sample_id;
#
#
# --
# -- Name: sample_type; Type: TABLE; Schema: public; Owner: sasan.sp92
# --
#
# CREATE TABLE public.sample_type (
#     sample_type_id integer NOT NULL,
#     type_name character(1) NOT NULL
# );
#
#
# ALTER TABLE public.sample_type OWNER TO "sasan.sp92";
#
# --
# -- Name: sample_type_sample_type_id_seq; Type: SEQUENCE; Schema: public; Owner: sasan.sp92
# --
#
# CREATE SEQUENCE public.sample_type_sample_type_id_seq
#     AS integer
#     START WITH 1
#     INCREMENT BY 1
#     NO MINVALUE
#     NO MAXVALUE
#     CACHE 1;
#
#
# ALTER TABLE public.sample_type_sample_type_id_seq OWNER TO "sasan.sp92";
#
# --
# -- Name: sample_type_sample_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: sasan.sp92
# --
#
# ALTER SEQUENCE public.sample_type_sample_type_id_seq OWNED BY public.sample_type.sample_type_id;
#
#
# --
# -- Name: test; Type: TABLE; Schema: public; Owner: sasan.sp92
# --
#
# CREATE TABLE public.test (
#     test_id integer NOT NULL,
#     test_name character(1) NOT NULL,
#     test_from_date date NOT NULL,
#     test_to_date date NOT NULL,
#     test_price integer NOT NULL,
#     reference_value character(1) NOT NULL
# );
#
#
# ALTER TABLE public.test OWNER TO "sasan.sp92";
#
# --
# -- Name: test_test_id_seq; Type: SEQUENCE; Schema: public; Owner: sasan.sp92
# --
#
# CREATE SEQUENCE public.test_test_id_seq
#     AS integer
#     START WITH 1
#     INCREMENT BY 1
#     NO MINVALUE
#     NO MAXVALUE
#     CACHE 1;
#
