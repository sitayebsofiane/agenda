--
-- PostgreSQL database dump
--

-- Dumped from database version 12.1
-- Dumped by pg_dump version 12.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: emira(text, text); Type: FUNCTION; Schema: public; Owner: postgres
--




CREATE TABLE public.events (
    id_event integer NOT NULL,
    id_user integer,
    title character varying(50),
    date timestamp without time zone,
    description text
);


ALTER TABLE public.events OWNER TO postgres;

--
-- Name: events_id_event_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.events_id_event_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.events_id_event_seq OWNER TO postgres;

--
-- Name: events_id_event_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.events_id_event_seq OWNED BY public.events.id_event;














CREATE TABLE public.roles (
    id_role integer NOT NULL,
    role_name character varying(20),
    role_description character varying(255)
);


ALTER TABLE public.roles OWNER TO postgres;

--
-- Name: roles_id_role_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.roles_id_role_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.roles_id_role_seq OWNER TO postgres;

--
-- Name: roles_id_role_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.roles_id_role_seq OWNED BY public.roles.id_role;


--
-- Name: user_agenda; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_agenda (
    id_user integer NOT NULL,
    name character varying(20),
    first_name character varying(20),
    password character varying(255)
);


ALTER TABLE public.user_agenda OWNER TO postgres;

--
-- Name: user_agenda_id_user_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_agenda_id_user_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_agenda_id_user_seq OWNER TO postgres;

--
-- Name: user_agenda_id_user_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_agenda_id_user_seq OWNED BY public.user_agenda.id_user;


--
-- Name: user_role; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_role (
    id_user_role integer NOT NULL,
    id_user integer,
    id_role integer
);


ALTER TABLE public.user_role OWNER TO postgres;

--
-- Name: user_role_id_user_role_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_role_id_user_role_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_role_id_user_role_seq OWNER TO postgres;

--
-- Name: user_role_id_user_role_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_role_id_user_role_seq OWNED BY public.user_role.id_user_role;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    firstname character varying(50) NOT NULL,
    pseudo character varying(50) NOT NULL,
    email character varying(250) NOT NULL,
    age integer NOT NULL,
    password character varying(250)
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: events id_event; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.events ALTER COLUMN id_event SET DEFAULT nextval('public.events_id_event_seq'::regclass);


--
-- Name: messages id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.messages ALTER COLUMN id SET DEFAULT nextval('public.messages_id_seq'::regclass);


--
-- Name: roles id_role; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roles ALTER COLUMN id_role SET DEFAULT nextval('public.roles_id_role_seq'::regclass);


--
-- Name: user_agenda id_user; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_agenda ALTER COLUMN id_user SET DEFAULT nextval('public.user_agenda_id_user_seq'::regclass);


--
-- Name: user_role id_user_role; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_role ALTER COLUMN id_user_role SET DEFAULT nextval('public.user_role_id_user_role_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: events; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.events (id_event, id_user, title, date, description) FROM stdin;
10	8	salam	2020-01-01 05:52:00	salam
11	8	farid	2020-01-01 05:52:00	farid
17	7	thomas	2020-01-01 05:52:00	
16	8	boxe	2020-05-05 05:52:00	ko



--
-- Data for Name: roles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.roles (id_role, role_name, role_description) FROM stdin;
4	USER	secritaire a le droit d'ajouter le titre et la date \n\t\t\t\t\t\t\t\tet de modifier uniqument ce qu'elle ajoute
1	ADMIN	big boss a le droit a tout
5	PUBLIC	public a le droit juste de voir
\.


--
-- Data for Name: user_agenda; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_agenda (id_user, name, first_name, password) FROM stdin;
3	bruno	bruno	660609b171607ff3dcd294929e5d8239736f4298
7	kevin	kevin	ffb4761cba839470133bee36aeb139f58d7dbaa9
8	farid	farid	6a214fde6c1f8c84902a5576bbe98834623913cc
9	turk	nicolas	01786cd22e6c8a15c447ae47312a353ae3919ee0
\.


--
-- Data for Name: user_role; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_role (id_user_role, id_user, id_role) FROM stdin;
3	7	4
5	8	1
6	9	1
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, name, firstname, pseudo, email, age, password) FROM stdin;
19	bruno	bruno	bruno	bruno	40	gAAAAABeIKd6_Iad4aYmBJOtr3irb69mprsLr1pmLfST6acITewi_ZWFNz2JMVOi3gx23rOnf3mxGEkBhkTJYTLHi05dn3ySRw==
21	kevin	thomas	apertura	toto@toto.fr	40	gAAAAABeIX8Mnq4xEcm94ThMwJAb41en1tPyfO9WKBEt1JHBiUJKHjrusw72jovUXqrfYqtj2UyhsL0SPFxyHeVkxaTmC56SGw==
20	reine_de_sql	reine_de_sql	reine_de_sql	reine_de_sql	41	gAAAAABeIKeY_LeQcwUx6J8jgnm3YwnkIZpSbJAwCTRlAaG8OB5Mu2trwLMu5cOo7Mz7X41nOZccpWBp0j97k80BRLCzIZFUdQ==
\.


--
-- Name: events_id_event_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.events_id_event_seq', 17, true);


--
-- Name: hibernate_sequence; Type: SEQUENCE SET; Schema: public; Owner: sofiane
--

SELECT pg_catalog.setval('public.hibernate_sequence', 1, false);


--
-- Name: messages_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.messages_id_seq', 19, true);


--
-- Name: roles_id_role_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.roles_id_role_seq', 5, true);


--
-- Name: user_agenda_id_user_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_agenda_id_user_seq', 12, true);


--
-- Name: user_role_id_user_role_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_role_id_user_role_seq', 8, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 21, true);


--
-- Name: events events_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_pkey PRIMARY KEY (id_event);


--
-- Name: messages messages_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_pkey PRIMARY KEY (id);


--
-- Name: roles roles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_pkey PRIMARY KEY (id_role);


--
-- Name: user_agenda user_agenda_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_agenda
    ADD CONSTRAINT user_agenda_pkey PRIMARY KEY (id_user);


--
-- Name: user_role user_role_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_role
    ADD CONSTRAINT user_role_pkey PRIMARY KEY (id_user_role);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users users_pseudo_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pseudo_key UNIQUE (pseudo);


--
-- Name: events events_id_user_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_id_user_fkey FOREIGN KEY (id_user) REFERENCES public.user_agenda(id_user);


--
-- Name: messages messages_id_auteur_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_id_auteur_fkey FOREIGN KEY (id_auteur) REFERENCES public.users(id);


--
-- Name: user_role user_role_id_role_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_role
    ADD CONSTRAINT user_role_id_role_fkey FOREIGN KEY (id_role) REFERENCES public.roles(id_role);


--
-- Name: user_role user_role_id_user_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_role
    ADD CONSTRAINT user_role_id_user_fkey FOREIGN KEY (id_user) REFERENCES public.user_agenda(id_user);


--
-- PostgreSQL database dump complete
--

